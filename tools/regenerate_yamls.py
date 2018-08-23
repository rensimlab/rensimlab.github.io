import numpy as np
import os
import yaml
import girder_client
import socket
import yt

def get_nice_size(my_size, fmt="%.2f"):
    prefs = ['', 'K', 'M', 'G', 'T',
             'P', 'E', 'Z', 'Y']
    exp = int(np.log(max(my_size, 1)) / np.log(1024))
    num = fmt % (my_size / 1024**exp)
    return "%s %sB" % (num, prefs[exp])

def listing_as_dict(listing):
    return dict((item['name'], item) for item in listing)

def get_rsc_id(gc):
    col_info = dict((col['name'], col)
                    for col in gc.listCollection())
    ren = col_info.get('Renaissance Simulations')
    if ren is None:
        raise RuntimeError("Couldn't get collection id!")
    return ren['_id']

def get_top_folder_id(gc, foldername):
    parent_id = get_rsc_id(gc)
    folders = gc.get(
        "/folder", parameters={'parentType': 'collection',
                               'parentId': parent_id})
    fol_info = listing_as_dict(folders)
    if foldername not in fol_info:
        raise RuntimeError(
            "Couldn't get folder id for %s." % foldername)
    return fol_info[foldername]['_id']

def get_top_folder(gc, foldername):
    parent_id = get_rsc_id(gc)
    folders = gc.get(
        "/folder", parameters={'parentType': 'collection',
                               'parentId': parent_id})
    fol_info = listing_as_dict(folders)
    if foldername not in fol_info:
        raise RuntimeError(
            "Couldn't get folder id for %s." % foldername)
    return fol_info[foldername]

def get_folder(gc, foldername):
    path = foldername.split(os.path.sep)
    folder = get_top_folder(gc, path.pop(0))
    while path:
        listing = gc.get('/folder/%s/listing' % folder['_id'])
        folder_data = listing_as_dict(listing['folders'])
        next_folder = path.pop(0)
        folder = folder_data.get(next_folder)
        if folder is None:
            raise RuntimeError("Folder %s not found in %s." % (next_folder, folder['name']))
    return folder

def get_folder_listing(gc, foldername, ltype=None):
    folder = get_folder(gc, foldername)
    listing = gc.get('/folder/%s/listing' % folder['_id'])
    if ltype is None:
        return listing
    return listing_as_dict(listing[ltype])

def get_listing(gc, fid, ltype=None):
    if isinstance(fid, dict):
        my_fid = fid['_id']
    else:
        my_fid = fid

    listing = gc.get('/folder/%s/listing' % my_fid)
    if ltype is None:
        return listing
    return listing_as_dict(listing[ltype])

def get_full_size(gc, foldername):
    if isinstance(foldername, dict):
        folder = foldername
    else:
        folder = get_folder(gc, foldername)

    listing = get_listing(gc, folder)
    size = folder['size']
    for subfolder in listing['folders']:
        size += get_full_size(gc, subfolder)
    return size

def set_rsl_entry(rdict, item):
    if item is None:
        return
    rdict['on_rsl'] = item['_id']
    rdict['size'] = get_nice_size(item['size'])

def do_for_rsl(entry):
    global reset_rsl
    return reset_rsl or not entry['on_rsl']

def do_for_gp(entry):
    global on_gp
    global reset_hc
    return on_gp and (reset_hc or entry['num_halos'] == 'N/A')

global on_gp
on_gp = socket.gethostname() == "galaxyportal"

global reset_hc
reset_hc = False

global reset_rsl
reset_rsl = False

data_dir = '/mnt/data/renaissance'
rsl_page_root = os.environ.get(
    'RSL_PAGE_ROOT', '/home/xarth/codes/rensimlab/rensimlab.github.io')

collectionPath = '/collection/Renaissance Simulations'
gc = girder_client.GirderClient(apiUrl='https://girder.rensimlab.xyz/api/v1')

server_paths = yaml.load(
    open(os.path.join(rsl_page_root, '_data', 'notebooks.yaml'), 'r'))
simulation_data = yaml.load(
    open(os.path.join(rsl_page_root, '_data', 'simulations.yaml'), 'r'))
description_data = yaml.load(
    open(os.path.join(rsl_page_root, '_data', 'descriptions.yaml'), 'r'))

for sim_name, sim in simulation_data.items():
    print ("Updating: ", sim_name)
    sim.update(description_data[sim_name])
    if do_for_rsl(sim):
        sim_folder = get_folder(gc, sim_name)
        set_rsl_entry(sim, sim_folder)
        sim['size'] = get_nice_size(get_full_size(gc, sim_folder))    

    hc_listing = get_folder_listing(gc, os.path.join("halo_catalogs", sim_name), 'folders')
    binary_folder = hc_listing.get('binary')
    if binary_folder is not None:
        binary_listing = get_listing(gc, binary_folder['_id'], 'folders')
    else:
        binary_listing = {}

    ascii_folder = hc_listing.get("ascii")
    set_rsl_entry(sim["ascii_halo_catalogs"], ascii_folder)
    if ascii_folder is not None:
        ascii_listing = get_listing(gc, ascii_folder['_id'], 'files')
    else:
        ascii_listing = {}

    if do_for_rsl(sim["binary_halo_catalogs"]):
        set_rsl_entry(sim["binary_halo_catalogs"], binary_folder)
        sim['binary_halo_catalogs']['size'] = \
          get_nice_size(get_full_size(gc, binary_folder))

    mt_folder = get_folder(gc, os.path.join("merger_trees", sim_name))
    mt_folders = get_listing(gc, mt_folder['_id'], 'folders')
    ytree_mt = mt_folders.get(sim_name.lower())
    set_rsl_entry(sim['ytree_merger_trees'], ytree_mt)
    mt_files = get_listing(gc, mt_folder['_id'], 'files')
    ct_mt = mt_files.get('tree_0_0_0.dat')
    set_rsl_entry(sim['ct_merger_trees'], ct_mt)

    sim_snaps = sim['snapshots']
    sim_listing = get_folder_listing(gc, sim_name, 'folders')
    for isnap, ds in enumerate(sim_snaps):
        snap_folder = sim_listing.get(ds['name'])
        set_rsl_entry(ds['snapshot'], snap_folder)

        if do_for_rsl(ds['binary_halo_catalogs']):
            hc_snap_folder = binary_listing.get(ds['name'])
            set_rsl_entry(ds['binary_halo_catalogs'], hc_snap_folder)
            ds['binary_halo_catalogs']['size'] = \
              get_nice_size(get_full_size(gc, hc_snap_folder))

        my_ascii = "out_%d.list" % isnap
        my_file = ascii_listing.get(my_ascii)
        set_rsl_entry(ds['ascii_halo_catalogs'], my_file)

        if on_gp and reset_hc:
            hcfn = os.path.join(data_dir, 'halo_catalogs', sim_name, 'binary',
                                ds['name'], "halos_%s.0.bin" % ds['name'])
            if os.path.exists(hcfn):
                myhc = yt.load(hcfn)
                ds['num_halos'] = myhc.index.total_particles

yaml.dump(
    simulation_data,
    open(os.path.join(rsl_page_root, '_data', 'simulations.yaml'), 'w'))

rafts = [
    {'id': _['_id'], 'name': _['name'], 'description': _['description']}
    for _ in gc.get('/raft')
]
yaml.dump(
    rafts,
    open(os.path.join(rsl_page_root, '_data', 'rafts.yaml'), 'w'))

welcome_rafts = dict((sim, False) for sim in simulation_data)
for sim in simulation_data:
    for raft in rafts:
        if raft['name'] == "Welcome to the %s Simulation" % sim:
            welcome_rafts[sim] = raft['id']
yaml.dump(welcome_rafts,
          open(os.path.join(rsl_page_root, '_data', 'welcome_rafts.yaml'), 'w'))

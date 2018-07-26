import numpy as np
import os
import yaml
import girder_client
import socket
import yt

def get_nice_size(my_size, fmt="%.2f"):
    prefs = ['', 'K', 'M', 'G', 'T',
             'P', 'E', 'Z', 'Y']
    exp = max(0, int(np.log(my_size) / np.log(1024)))
    num = fmt % (my_size / 1024**exp)
    return "%s %sB" % (num, prefs[exp])

def get_folder_info(gc, foldername):
    data = {}

    col_info = dict((col['name'], col)
                    for col in gc.listCollection())
    ren = col_info.get('Renaissance Simulations')
    if ren is None:
        raise RuntimeError("Couldn't get collection id!")
    parent_id = ren['_id']

    folders = gc.get(
        "/folder", parameters={'parentType': 'collection',
                               'parentId': parent_id})
    fol_info = dict((fol['name'], fol) for fol in folders)
    if foldername not in fol_info:
        raise RuntimeError(
            "Couldn't get folder id for %s." % foldername)
    fol_id = fol_info[foldername]['_id']

    listing = gc.get('/folder/%s/listing' % fol_id)
    for fol in listing['folders']:
        my_sim = fol['name'].split('_')
        sname = my_sim[0].title()
        if len(my_sim) > 1:
            sname += '_' + my_sim[1].upper()
        data[sname] = \
          {'on_rsl': fol['_id'],
           'size': get_nice_size(fol['size'])}
    return data

on_gp = socket.gethostname() == "galaxyportal"

data_dir = '/mnt/data/renaissance'
reset_hc = False

rsl_page_root = os.environ.get(
    'RSL_PAGE_ROOT', '/home/xarth/codes/rensimlab/rensimlab.github.io')

collectionPath = '/collection/Renaissance Simulations'
gc = girder_client.GirderClient(apiUrl='https://girder.rensimlab.xyz/api/v1')

server_paths = yaml.load(
    open(os.path.join(rsl_page_root, '_data', 'notebooks.yaml'), 'r'))
simulation_data = yaml.load(
    open(os.path.join(rsl_page_root, '_data', 'simulations.yaml'), 'r'))

for sim_name, sim in simulation_data.items():
    for ds in sim:
        ds['on_rsl'] = False
        ds['size'] = "N/A"

        if on_gp and (reset_hc or not ds['halo_catalogs']):
            hcfn = os.path.join(data_dir, 'halo_catalogs', sim_name,
                                "halos_%s.0.bin" % ds['snapshot'])
            if os.path.exists(hcfn):
                ds['halo_catalogs'] = True
                myhc = yt.load(hcfn)
                ds['num_halos'] = myhc.index.total_particles

    listing = gc.get('/folder/{}/listing'.format(server_paths[sim_name]))
    for folder in listing['folders']:
        try:
            pos = next((i for i, _ in enumerate(sim)
                        if folder['name'] == _['snapshot']))
            sim[pos]['on_rsl'] = folder['_id']
            sim[pos]['size'] = get_nice_size(folder['size'])
        except StopIteration:
            pass

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

for name in ["halo_catalogs", "merger_trees"]:
    data = get_folder_info(gc, name)
    ofn = os.path.join(rsl_page_root, '_data', '%s.yaml' % name)
    yaml.dump(data, open(ofn, 'w'))

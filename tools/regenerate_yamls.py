import os
import yaml
import girder_client
import socket
import yt

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
            sim[pos]['size'] = float("%.2f" % (folder['size']/1024**3))
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

import os
import yaml
import yt
import sys

data_dir = '/mnt/data/renaissance'

rsl_page_root = os.environ.get(
    'RSL_PAGE_ROOT', '/home/britton/rensimlab.github.io')

simyaml = os.path.join(rsl_page_root, '_data', 'simulations_new.yaml')
simulation_data = yaml.load(open(simyaml, 'r'))

if len(sys.argv) < 2:
    sys.exit()

sim = sys.argv[1]

fn = os.path.join(data_dir, sim, "rs_%s.h5" % sim.lower())
es = yt.load(fn)

on_rsl_def = {'on_rsl': False, 'size': 'N/A'}
def_entry = {"num_halos": 'N/A',
             "yt_halo_catalogs": on_rsl_def.copy(),
             "ascii_halo_catalogs": on_rsl_def.copy(),
             "snapshot": on_rsl_def.copy()}

sim_entries = [{"z": float("%.1f" % z), "name": os.path.dirname(myfn)}
               for z, myfn in zip(es.data["redshift"],
                                  es.data["filename"].astype(str))]
for entry in sim_entries:
    entry.update(def_entry)
simulation_data[sim] = sim_entries

yaml.dump(simulation_data, open(simyaml, 'w'))

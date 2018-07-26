import copy
import os
import yaml
import yt
import sys

data_dir = '/mnt/data/renaissance'

rsl_page_root = os.environ.get(
    'RSL_PAGE_ROOT', '/home/britton/rensimlab.github.io')

simyaml = os.path.join(rsl_page_root, '_data', 'simulations_new.yaml')
if os.path.exists(simyaml):
    simulation_data = yaml.load(open(simyaml, 'r'))
else:
    simulation_data = {}

if len(sys.argv) < 2:
    sys.exit()

sim = sys.argv[1]

fn = os.path.join(data_dir, sim, "rs_%s.h5" % sim.lower())
es = yt.load(fn)

on_rsl_def = {'on_rsl': False, 'size': 'N/A'}
def_entry = {"num_halos": 'N/A',
             "binary_halo_catalogs": copy.deepcopy(on_rsl_def),
             "ascii_halo_catalogs": copy.deepcopy(on_rsl_def),
             "snapshot": copy.deepcopy(on_rsl_def)}

sim_entries = [{"z": float("%.1f" % z), "name": os.path.dirname(myfn)}
               for z, myfn in zip(es.data["redshift"],
                                  es.data["filename"].astype(str))]
for entry in sim_entries:
    entry.update(copy.deepcopy(def_entry))
simulation_data[sim] = {}
simulation_data[sim]["ytree_merger_trees"] = copy.deepcopy(on_rsl_def)
simulation_data[sim]["ct_merger_trees"] = copy.deepcopy(on_rsl_def)
simulation_data[sim]["ascii_halo_catalogs"] = copy.deepcopy(on_rsl_def)
simulation_data[sim]["binary_halo_catalogs"] = copy.deepcopy(on_rsl_def)
simulation_data[sim]["snapshots"] = sim_entries

yaml.dump(simulation_data, open(simyaml, 'w'))

import copy
import os
import yaml
import yt
import sys

data_dir = '/mnt/data/renaissance'

rsl_page_root = os.environ.get(
    'RSL_PAGE_ROOT', '/home/britton/rensimlab.github.io')

simyaml = os.path.join(rsl_page_root, '_data', 'simulations.yaml')
if os.path.exists(simyaml):
    simulation_data = yaml.load(open(simyaml, 'r'))
else:
    simulation_data = {}

if len(sys.argv) < 2:
    sys.exit()

sim = sys.argv[1]

fn = os.path.join(data_dir, sim, "rs_%s.h5" % sim.lower())
es = yt.load(fn)

sim_entries = [{"z": float("%.2f" % z)}
               for z in es.data["redshift"]]
simulation_data[sim]["final_redshift"] = "%.2f" % es.data["redshift"][-1]
for i in range(len(sim_entries)):
    simulation_data[sim]["snapshots"][i].update(sim_entries[i])

yaml.dump(simulation_data, open(simyaml, 'w'))

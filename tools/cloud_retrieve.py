import argparse
import numpy as np
import os
import shutil
import signal
import subprocess
import sys
import tempfile
import yaml
import yt

def calculate_datasets(es, field, val_list, val_range):
    all_vals = es.data[field]
    esfns = es.data["filename"].astype(str)
    fns = []

    if val_list is not None:
        for value in val_list:
            i = np.argmin(np.abs(all_vals - value))
            fn = esfns[i]
            if fn not in fns:
                fns.append(fn)

    if val_range is not None:
        start, stop = val_range
        istart = np.argmin(np.abs(all_vals - start))
        istop  = np.argmin(np.abs(all_vals - stop ))
        inc = 1
        if istart > istop:
            inc = -1
        rfns = esfns[istart:istop+inc:inc]
        fns.extend([rfn for rfn in rfns if rfn not in fns])

    return fns

def download_dataset(cloud_object, cloud_path, data_path, timeout=None, tempdir=".", dryrun=False):
    yt.mylog.info("Downloading %s %s to %s." % (cloud_object, cloud_path, data_path))
    if dryrun: return

    curdir = os.getcwd()
    os.chdir(tempdir)

    command = "swift download %s -p %s" % (cloud_object, cloud_path)
    try:
        proc = subprocess.run(command, shell=True, timeout=timeout)
        if proc.returncode == 0:
            shutil.move(cloud_path, data_path)
        success = True
    except subprocess.TimeoutExpired:
        yt.mylog.error("Download of %s timedout after %d seconds." %
                       (cloud_path, timeout))
        success = False
    except KeyboardInterrupt:
        yt.mylog.error("Eject!")
        success = False

    if success:
        os.chdir(curdir)
    else:
        shutil.rmtree(cloud_path)
        os.chdir(curdir)
        sys.exit(0)

def gather_datasets(args, config):
    if args.redshift_list is None and args.redshift_range is None:
        raise RuntimeError(
            "Must specify either redshift-list or redshift-range.")
    if args.simulation not in config["simulations"]:
        raise RuntimeError(
            "%s not in available simulations: %s." %
            (args.simulation, ", ".join(config["simulations"])))

    esfn = os.path.join(config["data_dir"], args.simulation,
                        "rs_%s.h5" % args.simulation.lower())
    if not os.path.exists(esfn):
        raise RuntimeError("Simulation file not found: %s." % esfn)
    es = yt.load(esfn)

    fns = calculate_datasets(es, "redshift",
                             args.redshift_list, args.redshift_range)
    for fn in fns:
        dsfn = os.path.join(config["data_dir"], args.simulation, fn)
        if os.path.exists(dsfn):
            yt.mylog.info("%s already available, skipping." % fn)
        else:
            cloud_dir = os.path.join(
                config["simulations"][args.simulation]["cloud_directory"],
                os.path.dirname(fn))
            download_dataset(
                config["simulations"][args.simulation]["cloud_object"],
                cloud_dir, os.path.join(config["data_dir"], args.simulation),
                tempdir=config["temp_dir"], dryrun=args.dryrun)

if __name__ == "__main__":
    with open("renaissance.yml") as f:
        config = yaml.load(f)

    parser = argparse.ArgumentParser(
        description="Retrieve Renaissance simulation data from SDSC Cloud.")
    parser.add_argument("simulation", type=str,
                        help="The target simulation.")
    parser.add_argument("--redshift-list", type=float, nargs="+", metavar="z",
                        help="List of redshifts to retrieve. Example: 15 16 17")
    parser.add_argument("--redshift-range", type=float, nargs=2, metavar="z",
                        help="Redshift range to retrieve. Example: 15 20 for redshift 15-20")
    parser.add_argument("--dryrun", default=False, action="store_true",
                        help="Simulated run.  Do not actually download data.")
    args = parser.parse_args()

    gather_datasets(args, config)

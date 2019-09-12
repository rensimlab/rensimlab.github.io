# RSL Internal Documentation

- RSL front page: https://rensimlab.github.io/
- RSL girder page: https://girder.rensimlab.xyz/
- Github project: https://github.com/rensimlab/
    - front page repo: `rensimlab.github.io`
    - RSL Jupyter notebook docker file: `jupyter-rsl`
- Jupter notebook docker image: https://hub.docker.com/r/rensimlab/jupyter-rsl

The RSL front page is how the user is meant to approach the RSL. The girder page provides an admin interface for managing the data, users, and Jupyter sessions. The girder page is not intended to be seen by the user. The user interacts with the data by going to the **Investigate** page, selecting a specific simulation, and clicking on the **Launch Jupyter** or **Launch Tutorial** links.

The source for the front page is hosted on github in the *rensimlab* project space. The docker file describing the docker image used when starting a Jupyter session is also here. Editing the `Dockerfile` will trigger a rebuild of the image on dockerhub.

## RSL Admin

All RSL data is physically stored on `galaxyportal`. The girder setup is running there as well. One needs `sudo` privileges in order to start girder and modify the data hosted for the RSL.

### Starting up girder

Do the following:
```
$ sudo su - fido ; cd ~/hub ; docker-compose up -d
```

### Adding datasets to the RSL

#### Step 1: download data from SDSC cloud to galaxyportal

The Renaissance simulation data is stored on `galaxyportal` in `/mnt/data/renaissance`. There are directories for each simulation, all halo catalogs, and all merger-trees. Due to space limitations, only a small subset of all RS data is actively hosted. All RS data is stored in SDSC cloud in the following places:
- [Voids](https://object.cloud.sdsc.edu/v1/AUTH_normanlab/Renaissance/)
- [Normal regions](https://object.cloud.sdsc.edu/v1/AUTH_normanlab/Renaissance_Normal/)
- [Rarepeaks](https://object.cloud.sdsc.edu/v1/AUTH_normanlab/Renaissance_Rarepeak/)

It is not recommended to use the web interface to retrieve data. SDSC cloud has a default maximum filesize, above which a file is segmented into multiple parts. Segmented files cannot be downloaded from the web interface. You will get a file of zero size. Instead, the [swift](https://github.com/openstack/python-swiftclient) client provides a command-line interface. Within the [rensimlab.github.io](https://rensimlab.github.io/rensimlab.github.io) repository, there is a script that can be run from `galaxyportal` to automatically download datasets from SDSC cloud and put them in the correct place. This script has a few different options for getting data. Do the following to see what is available:
```
$ cd rensimlab.github.io/tools
$ python cloud_retrieve.py -h
```

Before running the `cloud_retrieve` script, you will need to be authenticated on SDSC cloud. The SDSC cloud admins should have provided you with a bash script to run to get authenticated. You'll need to run this everytime you login to `galaxyportal` to download data.

```
$ source normanlab-openrc.sh
Please enter your OpenStack Password for project normanlab as user USERNAME
```
After that, run `cloud_retrieve.py` with the appropriate options to download the data you want. Data will be downloaded to a temporary directory and then moved automatically to the correct location. Downloading a single dataset takes roughly 20 minutes.

#### Step 2: Ry-sync the girder database

The girder system is a database. It needs to be updated when data is added or removed. To resync, do the following:
```
$ sudo docker exec -ti hub_girder_1 /bin/bash
$ wget https://raw.githubusercontent.com/rensimlab/rensimlab.github.io/master/tools/syncer.py
$ girder-shell
```
The last command will start a Python interpreter. In there,  do the following:
```
In [1]: from syncer import sync
In [2]: sync()
```
This will sync the "Renaissance Simulations" collection, but not any other collections that someone with admin on the girder page might create.

#### Step 3: Update the RSL front pages

After step 2, new data will be visible from the girder page, but will not be listed on the RSL front page until the website repo has been updated. All of the information on the website about what data is available, how big it is, etc, comes from a series of YAML files that live in the `_data` directory within the front page repo. To update these, run the `regenerate_yamls.py` script in the `tools` directory of the front page repo.
```
cd rensimlab.github.io/tools
python regenerate_yamls.py
```
After this has run, type `git status` or `git diff` to see if any changes have been made to the YAML files. If so, commit the changes and push them to github.
```
git commit -am 'Updating yamls.'
git push origin master
```
You'll need write access on the github repo to do this. After that, the front page will automatically rebuild and reflect the changes.

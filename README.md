# Overview

# Installation

To start Girder, run the following:

```
$ sudo su - fido
$ cd ~/hub
$ docker-compose up -d
```

# Components

## RSL Website (rensimlab.github.io)

The RSL website is an interactive online "laboratory" hosted on GitHub Pages. It allows general user access to a limited amount of simulation data as well as the Jupyter analytics platform.

### Page Rendering

The contents of each subpage are stored in individual markdown files at the root directory of the [GitHub repository](https://github.com/rensimlab/rensimlab.github.io). At build, these are merged with the layout specified at the top of each document using Jekyll. For example, to specify that we want to serve the page `index.html` using the default layout, the line `layout: default` has been included at the start of `index.md`.

Layouts allow the website's universal static components, such as the vertical navigation panel and footer, to be displayed in a modular fashion alongside the custom page content specified in the markdown files. All layouts are available as HTML files with Liquid templating in the `/_layouts` directory. Learn more about the Liquid template language [here](https://shopify.github.io/liquid/).

Jekyll's behavior can be configured via `_config.yml`.

### Learn

This page describes the basic scientific premises that surround the Renaissance Simulations and the core functionality of the laboratory. The content of this page is editable via `learn.md`.

### Investigate

This page is a portal to access the 4 key components of each individual simulation: Jupyter Notebook analytics, redshift dumps, halo catalogs, and merger trees. The following simulations are currently available on the RSL:
- **Renaissance Simulations**
    - [Normal_BG](https://rensimlab.github.io/simulations/normal_bg.html)
    - [Normal_BG1](https://rensimlab.github.io/simulations/normal_bg1.html)
    - [Rarepeak](https://rensimlab.github.io/simulations/rarepeak.html)
    - [Rarepeak_LW](https://rensimlab.github.io/simulations/rarepeak_lw.html)
    - [Rarepeak_LWB](https://rensimlab.github.io/simulations/rarepeak_lwb.html)
    - [Void](https://rensimlab.github.io/simulations/void.html)
    - [Void_BG1](https://rensimlab.github.io/simulations/normal_bg.html)
- **Phoenix Simulations (TBA)**
    - PHX512
    - PHX256-1
    - PHX256-2

The content of this page is editable via `investigate.md`.

#### Simulations

Each simulation has a page that arranges all of the corresponding data in a table. From here, users can click a link to access either the blank Jupyter Notebook workspace or the tutorials. They are also able to download ZIPs of all of the data pertaining to this simulation available on `galaxyportal`.

All of the information displayed about the data within each simulation is determined by a set of automatically generated YAML files available in the `_data` directory. Upon adding any new data to the RSL's servers, these can be updated by running `tools/regenerate_yamls.py` and committing the changes. The pages will change dynamically due to templating.

### Showcase

This page describes various publications and pieces of media related to the Renaissance Simulations. The content of this page is editable via `showcase.md`.

### User Guide

This page describes background information that all users will need to effectively understand, navigate, and utilize both the data hosted on the RSL and the Jupyter analytics platform. The content of this page is editable via `user_guide.md`.

## Jupyter Notebooks

## Server (galaxyportal.sdsc.edu)

All RSL data is stored physically on `galaxyportal`. The server can be accessed by any authorized users via SSH and currently runs Ubuntu 18.04.5.

Any data from the Renaissance Simulations suite available for download on [rensimlab.github.io](rensimlab.github.io) is stored in `/mnt/data/renaissance`. For each simulation there exists an individual directory under its name containing the corresponding halo catalogs, merger trees, and redshift dumps.

### Girder ([girder.rensimlab.xyz](girder.rensimlab.xyz))

Girder is a data management platform that, for our purposes, serves as a middleman between user interactions with the RSL and the physical server's data. Girder creates a MongoDB representation of the files and structure in `galaxyportal` consisting of `Collections`, `Folders`, `Items`, and `Files` (listed in order of increasing specificity). Items are essentially pieces of complete data inside of the Girder database and thereby typically correspond to one File, with some exceptions. At the lowest level, Girder Files correspond to actual bytes in the physical server, albeit with some degree of abstraction. Girder `Assetstores` of type `Filesystem` represent a repository on the local filesystem of the physical server wherein the raw bytes of data are stored.

There are several advantages to adopting this model of data management, the most prominent of which is the ease at which Girder Items can be manipulated wherever needed without directly accessing and changing the raw data. The primary RSL interactions that Girder facilitates between client and server are through Jupyter Notebooks, where users are able to perform analytics on RSL data live. When users attempt to read a file at some path in the Jupyter Notebook, the FUSE filesystem in use for RSL, `girderfs` (available [here](https://github.com/data-exp-lab/girderfs)), translates their request into the physical path that corresponds to the Girder Item and then serves that resource to the user.

## SDSC Cloud

## Frontera and Ranch




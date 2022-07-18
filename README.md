# Overview

# Installation



# Components

## RSL Website (rensimlab.github.io)

The RSL website is an interactive online "laboratory" hosted on GitHub Pages. It allows general user access to a limited amount of simulation data as well as the Jupyter analytics platform.

### Rendering

The contents of each subpage are stored in individual markdown files at the root directory of the [GitHub repository](https://github.com/rensimlab/rensimlab.github.io). At build, these are merged with the layout specified at the top of each document using Jekyll. For example, to serve the page `index.html` using the default layout, the following segment has been included at the start of `index.md`:
```
---
layout: default
---
```
Layouts allow the website's universal static components, such as the vertical navigation panel and footer, to be displayed in a modular fashion alongside the custom page content specified in the markdown files. All layouts are available as HTML files with Liquid templating in the `/_layouts` directory. Learn more about the Liquid template language [here](https://shopify.github.io/liquid/).

Jekyll's behavior can be configured via `_config.yml`.

### Learn

This page describes the basic scientific premises that surround the Renaissance Simulations and the core functionality of the laboratory. The content of this page is editable via `learn.md`.

### Investigate

This page is a portal to access the 4 key components of each individual simulation: Jupyter Notebook analytics, redshift dumps, halo catalogs, and merger trees. The following simulations' data is currently available for public use on the RSL:
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

### Showcase

### User Guide

## Jupyter Notebooks

## Server (galaxyportal.sdsc.edu)

All RSL data is stored physically on `galaxyportal`. The server can be accessed by any authorized users via SSH and currently runs Ubuntu 18.04.5.

Any data from the Renaissance Simulations suite available for download on [rensimlab.github.io](rensimlab.github.io) are stored in `/mnt/data/renaissance`. For each simulation there exists an individual directory under its name that mimics the following file structure, where `X` is a placeholder for incremental numerical values:

```
Sim_Name/
├─ merger_trees/
│  ├─ sim_name/
│  │  ├─ sim_name_XXXX.h5
│  │  ├─ sim_name.h5
├─ RDXXXX
├─ rockstar_halos/
│  ├─ auto_rockstar.cfg
│  ├─ halos_RDXXXX.X.bin
│  ├─ halos_RDXXXX.X.particles
│  ├─ out_X.list
│  ├─ restart.cfg
│  ├─ rockstar.cfg
│  ├─ trees/
│  │  ├─ forests.list
│  │  ├─ locations.dat
│  │  ├─ tree_0_0_0.dat
├─ rs_sim_name.h5

```

## Girder ([girder.rensimlab.xyz](girder.rensimlab.xyz))



## SDSC Cloud

## Frontera





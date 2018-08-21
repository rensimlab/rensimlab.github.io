---

layout: default

mainpage: false

---

# Simulation details



## Initial Conditions
All of the Renaissance Simulations are performed in the same
comoving volume of (40 Mpc)<sup>3</sup>. The initial conditions for this
volume are generated using MUSIC [Hahn & Abel 2011](http://adsabs.harvard.edu/abs/2011MNRAS.415.2101H) with
second-order Lagrangian perturbations at z=99 using a 512<sup>3</sup>
root grid resolution. We use the cosmological parameters from
the seven-year WMAP ΛCDM+SZ+LENS best fit [Komatsu
et al. 2011](http://adsabs.harvard.edu/abs/2011ApJS..192...18K): Ω<sub>M</sub>=0.266, Ω<sub>Λ<sub>=0.734,
Ω<sub>b</sub>=0.0449, h=0.71, σ<sub>8</sub>=0.81, and n=0.963.

## Zoom-in Regions
It is computationally prohibitive to have the necessary
parsec-scale spatial resolution (and accompanying mass
resolution), which is required to marginally resolve star-forming
molecular clouds, throughout the entire simulation
volume. We perform zoom-in simulations on three selected
regions, ranging from 220 to 430 comoving Mpc<sup>3</sup> with
different overdensities, providing a mixture of large-scale
environments. We first run a 5123 N-body only simulation to
z = 6. We then select an overdense region (“Rarepeak”), a
nearly mean density region (“Normal”) and an underdense
region (“Void”), which are displayed in Figure 1. The selection
of the survey volume and detailed setup of the Rarepeak have
been described in [Xu et al. (2013)](http://adsabs.harvard.edu/abs/2013ApJ...773...83X), 
which is centered on two
3x10<sup>10</sup>M<sub>sun</sub> halos at z=6 with a survey volume of
(3.8 × 5.4 × 6.6) Mpc<sup>3</sup>. For both the Normal and Void runs,
we select comoving volumes of (6.0 × 6.0 × 6.125) Mpc<sup>3</sup> as
the survey volumes. We then re-initialize all simulations,
having the survey volume at the center, with three more static
nested grids to have an effective resolution of 4096<sup>3</sup> and an
effective dark matter mass resolution of 2.9×10<sup>4</sup>
M<sub>sun</sub> inside the highest static nested grid that encompasses the survey
volume.

## Adaptive Mesh Refinement
During the course of the simulation, we allow a
maximum refinement level of l=12, resulting in a maximal
resolution of 19 comoving parsecs. The refinement criteria
employed are the same as in [Wise et al. (2012b)](http://adsabs.harvard.edu/abs/2012MNRAS.427..311W), refining on
baryon and dark matter overdensities of four and local Jeans
length by at least four cells [Truelove et al. 1997](http://adsabs.harvard.edu/abs/1997ApJ...489L.179T) and is
restricted to the survey volumes. While the Rarepeak simulation
adjusts the survey volume size during the simulation to
contain only the highest resolution dark matter particles of the
highest static nested grid, matter in the Normal and Void
simulations is not fully contained in a large-scale potential well
and have significant peculiar velocities, causing some of the
high-resolution particles to migrate out of the initial static grid.
Thus, we simplify the simulation setup by restricting grid
refinement to occur in the initial high-resolution grid instead of
its Lagrangian region.

## Lyman-Werner Radiation
A total of 7 Renaissance Simulations listed on the [Investigate](investigate.html) page 
were performed with different treatments for the inclusion of Lyman-Werner UV radiation (10.2-13.6 eV)
which photodissociates molecular hydrogen, the primary coolant of 
primordial gas. In various combinations, they employ 2 different models for local
sources of LW radiation, and 2 different models for the Lyman-Werner radiation
background:

Model | Description
------|------------
LS1 | Lyman-Werner radiation from Pop III stars inside the simulated volume, geometrically attenuated.
LS2 | Lyman-Werner radiation from Pop III stars and metal-enriched star clusters inside the simulated volume, geometrically attenuated.
BG | Lyman-Werner background from early generations of Pop III stars based on the analytic model of [Wise & Abel (2005)](http://adsabs.harvard.edu/abs/2005ApJ...629..615W), as updated in [Wise et al. (2012)](http://adsabs.harvard.edu/abs/2012ApJ...745...50W).
BG1 | Lyman-Werner background is self-consistently computed from Pop III and metal-enriched stellar sources formed in the Normal simulation, as described in [Xu et al. (2016)](http://adsabs.harvard.edu/abs/2016ApJ...833...84X).

## Stopping Redshifts
We stop the simulations of the Rarepeak,
Normal, and Void regions at z=(15, 12.5, 8), respectively,
because of the high computational cost of the radiative transfer.
The Renaissance simulations were run on the Blue Waters
system at NCSA. Each simulation used approximately eight
million core-hours.

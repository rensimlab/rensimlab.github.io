---

layout: default

mainpage: false

---

# Simulation details



## initial conditions
All of the Renaissance Simulations are performed in the same
comoving volume of (40 Mpc)^3. The initial conditions for this
volume are generated using MUSIC (Hahn & Abel 2011) with
second-order Lagrangian perturbations at z=99 using a 512^3
root grid resolution. We use the cosmological parameters from
the seven-year WMAP ΛCDM+SZ+LENS best fit (Komatsu
et al. 2011): Ω_M=0.266, Ω_Λ=0.734, Ω_b=0.0449, h=0.71,
σ_8=0.81, and n=0.963.

## zoom-in regions
It is computationally prohibitive to have the necessary
parsec-scale spatial resolution (and accompanying mass
resolution), which is required to marginally resolve star-forming
molecular clouds, throughout the entire simulation
volume. We perform zoom-in simulations on three selected
regions, ranging from 220 to 430 comoving Mpc^3 with
different overdensities, providing a mixture of large-scale
environments. We first run a 5123 N-body only simulation to
z=6. We then select an overdense region (“Rarepeak”), a
nearly mean density region (“Normal”) and an underdense
region (“Void”), which are displayed in Figure 1. The selection
of the survey volume and detailed setup of the Rarepeak have
been described in Xu et al. (2013), which is centered on two
3×10^10M_sun halos at z=6 with a survey volume of
(3.8 × 5.4 × 6.6) Mpc**3. For both the Normal and Void runs,
we select comoving volumes of (6.0 × 6.0 × 6.125) Mpc^3 as
the survey volumes. We then re-initialize all simulations,
having the survey volume at the center, with threemore static
nested grids to have an effective resolution of 4096^3 and an
effective dark matter mass resolution of 2.9×10^4
M_sun inside the highest static nested grid that encompasses the survey
volume.

## adaptive mesh refinement
During the course of the simulation, we allow a
maximum refinement level ofl=12, resulting in a maximal
resolution of 19 comoving parsecs. The refinement criteria
employed are the same as in Wise et al. (2012b), refining on
baryon and dark matter overdensities of fourand local Jeans
length by at least fourcells (Truelove et al. 1998) and is
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

## stopping redshifts
We stop the simulations of the Rarepeak,
Normal, and Void regions at z=(15, 12.5, 8), respectively,
because of the high computational cost of the radiative transfer.
The Renaissance simulations were run on the Blue Waters
system at NCSA. Each simulation used approximately eight
million core-hours.
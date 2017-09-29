# Learn

This is where you can learn about the first galaxies in the universe, how we can
use supercomputers to study them, and what this site enables you to do.

 * Learn about the first galaxies in the universe

 * Learn about how we use supercomputers to study them

 * Learn about the Renaissance Simulations Laboratory

# The first galaxies in the universe

## Then and now

<figure style="display: table; float: right; margin: 0 0 20px 20px;">
<a href="somewhere">
<img src="images/fig1.png" width="320" style="float: right;"/></a>
<figcaption style="display: table-caption; caption-side: bottom;">
The Universe at t=13,800,000,000 yr (credit) (learn more)
</figcaption>
</figure>

The universe is filled with countless galaxies today. But there was a time not
long after the big bang when there were no galaxies at all—just tiny
fluctuations in the density of matter. How does a featureless universe “grow
galaxies”? And how do they differ from modern galaxies like the Milky Way?

<figure style="display: table; float: left;">
<a href="somewhereelse">
<img src="images/fig2.png" width="250"></a>
<figcaption style="display: table-caption; caption-side: bottom;">
The Universe at t=380,000,000 yr (credit) (learn more)
</figcaption>
</figure>

## Growing Galaxies

<figure style="display: table; float: right; margin: 0 0 20px 20px;">
<a href="somewhere">
<img src="images/fig3.png" width="320" style="float: right;"/></a>
<figcaption style="display: table-caption; caption-side: bottom;">
(credit) (learn more)
</figcaption>
</figure>

Gravity collects regions of slight overdensity in the early universe into dense
clumps of gas and dark matter cosmologists call halos. These halos merge and

coalesce to form the first galaxies (protogalaxies). As time goes on,
protogalaxies merge and coalesce into larger galaxies, and so on, until today we
have a variety of galaxy types and sizes. These include large spiral galaxies
like the Milky Way, and large elliptical galaxies, like M87. Thus, galaxies are
said to grow hierarchically, with large modern galaxies representing the
assembly of thousands of protogalaxies which are much smaller.

## Observing the First Galaxies

<figure style="display: table; float: right; margin: 0 0 20px 20px;">
<a href="somewhere">
<img src="images/fig4.png" width="320" style="float: right;"/></a>
<figcaption style="display: table-caption; caption-side: bottom;">
(credit) (learn more)
</figcaption>
</figure>

Can we observe the first galaxies directly? No. They are too small and too faint
for the Hubble Space Telescope (HST) to detect them. However the HST can detect
very faint, distant galaxies which are likely second and third generation
galaxies. The graphic at right shows how deep the HST has been able to probe.
The Hubble Ultra Deep Field  has detected galaxies when the universe was only
400-700 million years old, which is only a few percent of its present age.

The James Webb Space Telescope, to be launched by NASA in 2018, should be able
to observe even younger galaxies, pushing into the realm of truly first
galaxies.

## Faint Red Blobs at the Edge of the Universe

<figure style="display: table; float: right; margin: 0 0 20px 20px;">
<a href="somewhere">
<img src="images/fig5.png" width="320" style="float: right;"/></a>
<figcaption style="display: table-caption; caption-side: bottom;">
(credit) (learn more)
</figcaption>
</figure>

While not strictly the first galaxies in the universe, the most distant galaxies
detected by the HST are worthy of study. They appear as faint red blobs in the
Hubble Ultra Deep Field. They are red because the expansion of the universe has
redshifted their starlight into the red part of the visible spectrum. They are
faint because they are distant. And they are very small compared to the Milky
Way galaxy. A typical size is about 500 parsec, which is 1/50 the size of the
Milky Way galaxy.

# How we use supercomputers to study the first galaxies

Before we delve into how we use supercomputers to study the first galaxies, we need
to cover some basics. 

## Supercomputers
<figure style="display: table; float: right; margin: 0 0 20px 20px;">
<a href="somewhere">
<img src="images/fig5.png" width="320" style="float: right;"/></a>
<figcaption style="display: table-caption; caption-side: bottom;">
(credit) (learn more)
</figcaption>
</figure>

Supercomputers are large clusters of processing “nodes” all connected together by 
a fast network so that it can act like a single, very powerful computer. Each node 
can have dozens of processing “cores”. For example, The Blue Waters supercomputer, 
used for the Renaissance Simulations, has over 22,640 nodes, each with 16 cores, for 
a total of 362,240  processing elements. 

## Parallel computing
<figure style="display: table; float: right; margin: 0 0 20px 20px;">
<a href="somewhere">
<img src="images/fig5.png" width="320" style="float: right;"/></a>
<figcaption style="display: table-caption; caption-side: bottom;">
(credit) (learn more)
</figcaption>
</figure>

Supercomputers are programmed using a technique called parallel computing. Quite 
simply, a large problem (like computing the universe) is subdivided into many smaller 
problems (like compute this piece of the universe), and each smaller problem is assigned 
to one of the computing cores or nodes. All these smaller problems are computed 
simultaneously, or “in parallel”, with information about their state being continuously 
communicated to neighboring processors in order to maintain physical correctness and 
synchronicity. Typically, the subdivision of the big problem into many smaller problems 
is done using domain decomposition, illustrated at right.  

Adding more


### Extra

<iframe width="560" height="315" src="https://www.youtube.com/embed/IKUGyy6DoTE" frameborder="0" allowfullscreen></iframe>

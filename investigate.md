---
layout: default
mainpage: true
order: 3
---

# Investigate

This is the place to access and analyze data from the Renaissance Simulations.
Below is a table of all simulations comprising the Renaissance Simulation
suite, including a list of all publications to make use of each data set. All
simulations were initialized at redshift 99, but each was run down to a
different final redshift, as indicated in the table. The table also gives the
models used for including Lyman-Werner radiation from local and background
sources. See [here](sim_details.html) for a full, technical description of the
simulations.

Each link in the table will take you to a page containing further details of
that particular simulation as well as links to download full snapshots, halo
catalogs, and merger trees. The pages also contains links to launch Jupyter
notebook sessions that will allow you to work with all available data using
[yt](https://yt-project.org/) and [ytree](https://ytree.readthedocs.io/).
You will be provided with persistent storage space with which to save
analysis scripts and results. For more information on running analysis on
the RSL, see the [User Guide](user_guide.html).

<TABLE>
  <TR>
    <TH>Simulation</TH>
    <TH>Local Lyman-Werner
    <a href="../sim_details.html#lwr"><i class="fa fa-info-circle fa-fw" title="more info"></i></a></TH>
    <TH>Background Lyman-Werner
    <a href="../sim_details.html#lwr"><i class="fa fa-info-circle fa-fw" title="more info"></i></a></TH>
    <TH>Final Redshift</TH>
    <TH>Publications</TH>
  </TR>
{% for sim in site.data.simulations %}
  <TR>
    <TD><a href="simulations/{{ sim[0] | downcase }}.html">{{ sim[0] }}</a></TD>
    <TD>{{ sim[1]['Lyman-Werner']['local'] }}</TD>
    <TD>{{ sim[1]['Lyman-Werner']['background'] }}</TD>
    <TD>{{ sim[1]['final_redshift'] }}</TD>
    <TD>
{% assign first = "true" %}{% for i in (0..site.data.publications.size) %}{% assign pub = site.data.publications[i] %}{% if pub['simulations'] contains sim[0] %}{% if first == "true" %}{{ i | plus: 1 }}{% assign first = "false" %}{% else %}, {{ i | plus: 1 }}{% endif %}{% endif %}{% endfor %}
    </TD>
  </TR>
{% endfor %}
</TABLE>

## Publications

<ol>
{% for pub in site.data.publications %}
<li><a href="{{ pub['url'] }}">"{{ pub['title'] }}"</a>, {{ pub['authors'] }}, {{ pub['year'] }}, {{pub['journal']}}.</li>
{% endfor %}
</ol>

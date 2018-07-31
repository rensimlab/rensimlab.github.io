---
layout: default
mainpage: true
order: 3
---

# Investigate

Describe!

## Available Data

<TABLE>
  <TR>
    <TH>Simulation</TH>
    <TH>Final Redshift</TH>
    <TH>Publications</TH>
  </TR>
{% for sim in site.data.simulations %}
  <TR>
    <TD><a href="simulations/{{ sim[0] | downcase }}.html">{{ sim[0] }}</a></TD>
    <TD>{{ sim[1]['final_redshift'] }}</TD>
    <TD></TD>
  </TR>
{% endfor %}
</TABLE>

## Publications

<ol>
{% for pub in site.data.publications %}
<li><a href="{{ pub['url'] }}">"{{ pub['title'] }}"</a>, {{ pub['authors'] }}, {{ pub['year'] }}, {{pub['journal']}}.</li>
{% endfor %}
</ol>

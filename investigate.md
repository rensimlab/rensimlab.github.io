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
    <TD>
{% assign first = "true" %}
{% for i in (0..site.data.publications.size) %}{% assign pub = site.data.publications[i] %}{% if pub['simulations'] contains sim[0] %}{% if first == "true" %}{{ i | plus: 1 }}{% assign first = "false" %}{% else %}, {{ i | plus: 1 }}
{% endif %}{% endif %}{% endfor %}
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

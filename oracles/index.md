---
layout: default
---

# Oracles

{% for file in site.static_files %}
{% if file.path contains "/oracles/" %}
{% assign robot = file.basename | split: "." %}
{% if current_robot != robot[0] %}

## {{ robot[0] }}

{% endif %}

{% if file.extname == ".svg" %}

![{{ robot[0] }}]({{ site.baseurl }}{{ file.path }})

{% else %}

- [{{file.name}}]({{ site.baseurl }}{{ file.path }})

{% endif %}


{% assign current_robot = robot[0] %}
{% endif %}
{% endfor %}

---
layout: default
---

{% assign files = site.static_files | sort: "file.path" %}

{% for file in files %}


{% if file.path contains page.dir %}
{% assign robot = file.basename | split: "." %}
{% assign path =  file.path | remove: file.name %}
{% assign struct = path | split: "/" %}
{% if current_robot != struct[-1] %}

{% assign level = struct.size | minus: 1 %}

<h{{ level }}> {{ struct[-1] | capitalize }} </h{{ level }}>


{% endif %}

{% if file.extname == ".svg" %}

![{{file.name}}]({{ site.baseurl }}{% link {{file.path}} %})

{% else %}
- [{{file.name}}]({{ site.baseurl }}{% link {{file.path}} %})
{% endif %}


{% assign current_robot = struct[-1] %}
{% endif %}
{% endfor %}

---
layout: default
---

# ExSce Models

{% for item in site.data.file_paths%}
## `{{ item[0]  }}`
{% for file_data in item[1] %}
- [{{ file_data.path }}]({{ file_data.path }})
{% endfor %}
{% endfor %}

<table id="models" class="table table-striped" style="width:100%">
<thead>
<tr>
<th>Filename</th>
<th>Extension</th>
<th>Path</th>
</tr>
</thead>
<tbody>
{% for item in site.data.file_paths%}
{% for file_data in item[1] %}
<tr>
<td>{{ file_data[1] }}</td>
<td>{{ file_data[0] }}</td>
<td><a href="{{ file_data[2] }}">{{ file_data[2] }}</a></td>
</tr>
{% endfor %}
{% endfor %}
</tbody>
</table>

<script src="https://code.jquery.com/jquery-3.5.1.js"></script>
<script src="https://cdn.datatables.net/1.13.5/js/jquery.dataTables.min.js"></script>
<script src="https://cdn.datatables.net/1.13.5/js/dataTables.bootstrap5.min.js"></script>
<script>
new DataTable('#models');
</script>

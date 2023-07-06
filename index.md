---
layout: default
---

# ExSce Models

In the below table are all the models created during the development
of the ExSce Workbench. They are referred to from the various tutorials
listed on the
[Repository of Executable Scenarios](https://sesame-project.github.io/exsce/exsce-repo.html).

<table id="models" class="table table-striped" style="width:100%;white-space:nowrap;">
<thead>
<tr>
<th>Filename</th>
<th>Extension</th>
<th>Path</th>
<th style="display:none"></th>
</tr>
</thead>
<tbody>
{% for item in site.data.file_paths%}
{% for file_data in item[1] %}
<tr>
<td>
  {{ file_data.name }}
</td>
<td>
  {{ file_data.extension }}
</td>
<td>
  <a href="{{ file_data.path }}">{{ file_data.path }}</a>
</td>
<td style="display:none">
{{ item[0]  }}
</td>
</tr>
{% endfor %}
{% endfor %}
</tbody>
</table>

<script src="assets/js/jquery-3.5.1.min.js"></script>
<script src="assets/js/jquery.dataTables.min.js"></script>
<script src="assets/js/dataTables.bootstrap5.min.js"></script>
<script src="assets/js/dataTables.rowGroup.min.js"></script>
<script>
new DataTable('#models', {
    scrollX: true,
    order: [[2, 'asc']],
    rowGroup: {
        dataSrc: 3
    }
});
</script>

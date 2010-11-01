function increment_form_ids(el, to) { 
    var from = to-1;
	var total_form = parseInt($("#id_events-TOTAL_FORMS")[0].value);
    var new_total = total_form + 1
	$("#id_events-TOTAL_FORMS")[0].value = new_total.toString()
    $(':input', $(el)).each(function(i,e){
          var old_name = $(e).attr('name')
          var old_id = $(e).attr('id')
          $(e).attr('name', old_name.replace(from, to))
          $(e).attr('id', old_id.replace(from, to))
          $(e).val('')
    })
}
 
function add_inline_button() {
    $("p.tools a.add").bind("click", function(e) {
        var rows = $(this).parents("form").find("div.inline-group").find("table");
		var last = $(rows[rows.length-1]);
        var copy = last.clone(true);
		last.after(copy);
        $($(this).parents("div.inline-group").find("input")[0]).val(rows.length+1);
        increment_form_ids(copy, rows.length);
        return false;
    });
}

$(document).ready(add_inline_button);


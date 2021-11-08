{
	const initCheckbox2 = (obj_name, checkbox_name, disp) => {
		const func = () => document.getElementById(obj_name).style.display = document.getElementById(checkbox_name).checked ? disp : "none";
		initCheckbox(checkbox_name, func);
		func();
	}

	initCheckbox2("wrap-content-editor", "show_edit_checkbox", "grid");
	initCheckbox2("wrap-content-view", "show_result_checkbox", "block");
	initCheckbox2("wrap_content_html", "show_html_checkbox", "block");
	initCheckbox2("wrap_content_css", "show_css_checkbox", "block");
	initCheckbox2("wrap_content_js", "show_js_checkbox", "block");
}

function changeSiteContent(data) {
	$("#content_html").value = data["html"];
	$("#content_css").value = data["css_text"];
	$("#content_js").value = data["js_text"];
	$("#content_header").value = document.title = data["title"];
	$("#content_list").innerHTML = data["content_list"];
	addScript(data["js_url"]);
	addStyle(data["css_url"]);
}

initCheckbox("edit_checkbox", () => window.location.reload());

function save_page_data() {
	if (confirm("Сохранить содержимое страницы?") === false)
		return;
	let data = new FormData();
	data.append('page', pageNow());
	data.append('page_name', $("#content_header").value);
	data.append('data', $("#content_html").value);
	data.append('css', $("#content_css").value);
	data.append('js', $("#content_js").value);
	data.append('csrfmiddlewaretoken', csrftoken);
	fetch("/save_page/", {
		method: 'POST',
		body: data,
		credentials: 'same-origin',
	})
		.then((data) => {
			if ($("#ajax_checkbox").checked)
				changeSiteContent(getPageData(pageNow()));
			else
				window.location.reload();
		})
}

setInterval((() => {
	let value_html = $("#content_html").value
	let value_css = $("#content_css").value
	return () => {
		let new_value_html = $("#content_html").value
		let new_value_css = $("#content_css").value
		if ((value_html != new_value_html) || (value_css != new_value_css)){
			value_html = new_value_html;
			value_css = new_value_css;
			$("#content_view").innerHTML = `<style>${value_css}</style>${value_html}`;
		}
	}
})(), 60)

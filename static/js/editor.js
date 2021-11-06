function changeSiteContent(data) {
	$("#content").value = data["content_text"];
	$("#content_header").value = document.title = data["title"];
	$("#content_list").innerHTML = data["content_list"];
}

initCheckbox("edit_checkbox", () => window.location.reload());

const __f_se_chkb = () => {
	$("#wrap-content-editor").style.display = $("#show_edit_checkbox").checked ? "block" : "none";
};
initCheckbox("show_edit_checkbox", __f_se_chkb);
__f_se_chkb();

const __f_sr_chkb = () => {
	$("#wrap-content-view").style.display = $("#show_result_checkbox").checked ? "block" : "none";
};
initCheckbox("show_result_checkbox", __f_sr_chkb);
__f_sr_chkb();

function save_page_data() {
	if (confirm("Сохранить содержимое страницы?") === false)
		return;
	let data = new FormData();
	data.append('page', decodeURI(document.URL.split('=')[1]));
	data.append('page_name', $("#content_header").value);
	data.append('data', $("#content").value);
	data.append('csrfmiddlewaretoken', csrftoken);
	fetch("/save_page/", {
		method: 'POST',
		body: data,
		credentials: 'same-origin',
	})
		.then((data) => {
			if ($("#ajax_checkbox").checked === false)
				window.location.reload();
			else
				changeSiteContent(getPageData(decodeURI(document.URL.split('=')[1])));
		})
}

function windowResize() {
	$("#content_view").style.height = (window.innerHeight - 227) + "px";
	$("#content").style.height = (window.innerHeight - 227) + "px";
};

window.addEventListener('resize', windowResize);
windowResize();

var content_value = $("#content").value;
setInterval(() => {
	let v = $("#content").value
	if (content_value != v) {
		content_value = v;
		$("#content_view").innerHTML = v;
	}
}, 60)

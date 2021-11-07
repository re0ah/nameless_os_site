function changeSiteContent(data) {
	$("#content_html").value = data["html"];
	$("#content_css").value = data["css_text"];
	$("#content_js").value = data["js_text"];
	$("#content_header").value = document.title = data["title"];
	$("#content_list").innerHTML = data["content_list"];
}

initCheckbox("edit_checkbox", () => window.location.reload());

function __f_chkb(obj, chkb) {
	return () => obj.style.display = chkb.checked ? "block" : "none";
};
const __f_se_chkb = __f_chkb($("#wrap-content-editor"), $("#show_edit_checkbox"));
initCheckbox("show_edit_checkbox", __f_se_chkb);
__f_se_chkb();

const __f_sr_chkb = __f_chkb($("#wrap-content-view"), $("#show_result_checkbox"));
initCheckbox("show_result_checkbox", __f_sr_chkb);
__f_sr_chkb();

function save_page_data() {
	if (confirm("Сохранить содержимое страницы?") === false)
		return;
	let data = new FormData();
	data.append('page', decodeURI(document.URL.split('=')[1]));
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
				changeSiteContent(getPageData(decodeURI(document.URL.split('=')[1])));
			else
				window.location.reload();
		})
}

function windowResize() {
	$("#content_view").style.height = (window.innerHeight - 227) + "px";
	$("#content_html").style.height = ((window.innerHeight - 309) / 3) + "px";
	$("#content_css").style.height = ((window.innerHeight - 309) / 3) + "px";
	$("#content_js").style.height = ((window.innerHeight - 309) / 3) + "px";
};

window.addEventListener('resize', windowResize);
windowResize();

let v_html = $("#content_html").value
let v_css = $("#content_css").value
setInterval(() => {
	let _v_html = $("#content_html").value
	let _v_css = $("#content_css").value
	if ((v_html != _v_html) || (v_css != _v_css)){
		v_html = _v_html;
		v_css = _v_css;
		$("#content_view").innerHTML = `<style>${v_css}</style>` + v_html;;
	}
}, 60)

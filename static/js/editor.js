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

const changeEditorHandler = function() {
	let value_html = $("#content_html").value
	let value_css = $("#content_css").value
	$("#content_view").innerHTML = `<style>${value_css}</style>${value_html}`;
}

$("#content_html").addEventListener("input", changeEditorHandler);
$("#content_css").addEventListener("input", changeEditorHandler);

function changeSiteContent(data) {
	$("#content_html").value = data["html"];
	$("#content_css").value = data["css_text"];
	$("#content_js").value = data["js_text"];
	$("#content_header").value = document.title = data["title"];
	$("#content_list").innerHTML = data["content_list"];
	addScript(data["js_url"]);
	addStyle(data["css_url"]);
	changeEditorHandler();
}

async function save_page_data() {
	if (confirm("Сохранить содержимое страницы?") === false)
		return;
	let data = new FormData();
	data.append('page', pageNow());
	data.append('page_name', $("#content_header").value);
	data.append('data', $("#content_html").value);
	data.append('css', $("#content_css").value);
	data.append('js', $("#content_js").value);
	data.append('csrfmiddlewaretoken', csrftoken);
	let response = await fetch("/save_page/", {
		method: 'POST',
		body: data,
		credentials: 'same-origin',
	})
	if (await response.status === 200)
		if ($("#ajax_checkbox").checked)
			changeSiteContent(await getPageData(pageNow()));
		else
			window.location.reload();
}


/*
function appendLine(textarea, lines) {
	function updateLines() {
		const line_count = textarea.value.split("\n").length;
		const child_count = lines.children.length;
		let diff = line_count - child_count;
		if(diff > 0) {
			const fragment = document.createDocumentFragment();
			for (let i = diff; i > 0; i--) {
				const line_number = document.createElement("span");
				line_number.className = "tln-line";
				fragment.appendChild(line_number);
			}
			lines.appendChild(fragment);
		}
		else {
			for (let i = diff; i < 0; i++) {
				lines.removeChild(lines.lastChild);
			}
		}
	}

	updateLines(textarea, lines);

	const changeHandler = ((textarea, lines) => () => {
		updateLines(textarea, lines);
		console.log("change");
	})(textarea, lines);
	textarea.addEventListener("input", changeHandler);

	const scrollHandler = ((textarea, lines) => () => {
		lines.scrollTop = textarea.scrollTop;
		console.log("scroll");
	})(textarea, lines);
	const scrollEvents = ["change", "mousewheel", "scroll"];
	[...scrollEvents].forEach((scrollEvent) => {
		textarea.addEventListener(scrollEvent, scrollHandler);
	});
}

appendLine($("#content_html"), $("#TLN_LEFT_HTML"));
*/

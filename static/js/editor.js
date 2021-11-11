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

const updateLines = (textarea, lines) => () => {
	const diff = textarea.value.split("\n").length - lines.children.length;
	if(diff > 0) {
		const fragment = document.createDocumentFragment();
		for (let i = diff; i > 0; i--) {
			const line = document.createElement("span");
			line.className = `text-area-line ${textarea.name}`;
			fragment.appendChild(line);
		}
		lines.appendChild(fragment);
	}
	else {
		for (let i = diff; i < 0; i++) {
			lines.removeChild(lines.lastChild);
		}
	}
};

function initTextAreaLines(textarea, lines, updateLinesCallback) {
	updateLinesCallback();

	textarea.addEventListener("input", updateLinesCallback());

	const scrollHandler = ((textarea, lines) => () => {
		lines.scrollTop = textarea.scrollTop;
	})(textarea, lines);
	const scrollEvents = ["change", "mousewheel", "scroll"];
	[...scrollEvents].forEach((scrollEvent) => {
		textarea.addEventListener(scrollEvent, scrollHandler);
	});
}

const updateLinesHtml = updateLines($("#content_html"), $("#lines_html"));
const updateLinesCss = updateLines($("#content_css"), $("#lines_css"));
const updateLinesJs = updateLines($("#content_js"), $("#lines_js"));
initTextAreaLines($("#content_html"), $("#lines_html"), updateLinesHtml);
initTextAreaLines($("#content_css"), $("#lines_css"), updateLinesCss);
initTextAreaLines($("#content_js"), $("#lines_js"), updateLinesJs);

const changeEditorHandler = function() {
	let value_html = $("#content_html").value
	let value_css = $("#content_css").value
	$("#content_view").innerHTML = `<style>${value_css}</style>${value_html}`;
	$("#content_html"), $("#lines_html");
	eval($("#content_js").value);
}
$("#content_html").addEventListener("input", changeEditorHandler);
$("#content_html").addEventListener("input", updateLinesHtml);

$("#content_css").addEventListener("input", changeEditorHandler);
$("#content_css").addEventListener("input", updateLinesCss);

$("#content_js").addEventListener("input", updateLinesJs);

function changeSiteContent(data) {
	$("#content_html").value = data["html"];
	$("#content_css").value = data["css_text"];
	$("#content_js").value = data["js_text"];
	$("#content_header").value = document.title = data["title"];
	$("#content_list").innerHTML = data["content_list"];
	updateLinesHtml();
	updateLinesCss();
	updateLinesJs();
	changeEditorHandler();
	eval(data["js_text"]);
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
	const response = await fetch("/save_page/", {
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

function initFontSizeTextarea(textarea, lines, size) {
	textarea.style.fontSize = size;
	document.documentElement.style.setProperty(lines, size); // lines textarea
}

function initFontInput(inputId) {
	const el = $(`#${inputId}`);
	let fontSize = getCookie(inputId) 
	el.value = (fontSize === null) ? "16" : fontSize;

	const fontInput = function() {
		document.cookie = `${this.id}=${this.value}`;
		initFontSizeTextarea($(`#${this.name}`), this.lang, `${this.value}px`);
	}
	fontInput.call(el);

	el.addEventListener("input", fontInput);
	el.addEventListener("mousewheel", (e) => {console.log(e)});
}
initFontInput("html_font_size");
initFontInput("css_font_size");
initFontInput("js_font_size");

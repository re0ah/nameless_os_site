function getCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i=0;i < ca.length;i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1,c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
    }
    return null;
}

var $ = document.querySelector.bind(document);

function checkAuthorization() {
	var xhr = new XMLHttpRequest();
	xhr.open("GET", `/check_authorization/`, false);
	xhr.send(null);
	return JSON.parse(xhr.responseText)["state"];
}

console.log("checkauth", checkAuthorization());

function setCheckboxValue(checkbox, value) {
	if (value === null)
		return
	if (checkbox.checked != value) {
		checkbox.click();
	}
}

function initCheckbox(checkbox_id, func) {
	let el = $(`#${checkbox_id}`);
	setCheckboxValue(el, getCookie(checkbox_id) === "true");
	el.addEventListener("click", function () {
		document.cookie = `${this.id}=${this.checked}`;
		func();
	})
}

initCheckbox("ajax_checkbox", () => window.location.reload());
initCheckbox("cache_checkbox", () => {});

function changeSiteContent(data) {
	$("#content").innerHTML = data["content_text"];
	$("#content_header").innerHTML = document.title = data["title"];
	$("#content_list").innerHTML = data["content_list"];
}

function ajaxPageData(pageName) {
	var xhr = new XMLHttpRequest();
	xhr.open("GET", `?page=${pageName}&is_ajax=true`, false);
	xhr.send(null);
	if($("#cache_checkbox").checked) {
		sessionStorage.setItem(pageName, xhr.responseText);
	}
	return JSON.parse(xhr.responseText);
}

function getPageData(pageName) {
	if($("#cache_checkbox").checked) {
		let data = JSON.parse(sessionStorage.getItem(pageName));
		return data ? data : ajaxPageData(pageName);
	}
	return ajaxPageData(pageName);
}

function ajaxUpdatePage(pageName) {
	if (decodeURI(document.URL.split('=')[1]) === pageName)
		return;

	let data = getPageData(pageName);
	changeSiteContent(data);
	window.history.pushState(pageName, data["title"], `?page=${pageName}`);
}

window.addEventListener('popstate', (e) => {
	let data = getPageData(e.state ? e.state : "Главная страница");
	changeSiteContent(data);
})

function windowResize() {
	$("#content_wrap").style.maxHeight = (window.innerHeight - 100) + "px";
	$("#content").style.maxHeight = (window.innerHeight - 170) + "px";
};

window.addEventListener('resize', windowResize);
windowResize();

var $ = document.querySelector.bind(document);

function addScript(src) {
    var s = document.createElement('script');
    s.type = 'text/javascript';
    s.src = src;
    document.getElementsByTagName('head')[0].appendChild(s);
    return s;
}

function addStyle(src) {
    var s = document.createElement('link');
    s.rel = 'stylesheet';
    s.href = src;
    document.getElementsByTagName('head')[0].appendChild(s);
    return s;
}

function checkAuthorization() {
	var xhr = new XMLHttpRequest();
	xhr.open("GET", `/check_authorization/`, false);
	xhr.send(null);
	return JSON.parse(xhr.responseText)["state"];
}

function changeSiteContent(data) {
	$("#content").innerHTML = data["html"];
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
	addScript(data["js_url"]);
	addStyle(data["css_url"]);
	window.history.pushState(pageName, data["title"], `?page=${pageName}`);
}

window.addEventListener('popstate', (e) => {
	let data = getPageData(e.state ? e.state : "Главная страница");
	changeSiteContent(data);
})

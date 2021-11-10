var $ = document.querySelector.bind(document);

const addScript = (() => {
	let script_now;
	return (src) => {
		if(script_now !== undefined)
		    document.getElementsByTagName('head')[0].removeChild(script_now);
    	script_now = document.createElement('script');
    	script_now.type = 'text/javascript';
    	script_now.src = src;
    	document.getElementsByTagName('head')[0].appendChild(script_now);
	}
})();

const addStyle = (src) => $("#load_css").href = src;

function changeSiteContent(data) {
	$("#content").innerHTML = `<style>${data["css_text"]}</style>` + data["html"];
	$("#content_header").innerHTML = document.title = data["title"];
	$("#content_list").innerHTML = data["content_list"];
	eval(data["js_text"]);
}

async function checkAuthorization() {
	const request = await fetch("/check_authorization/");
	return await request.status;
}

async function getJson(url, storageKey) {
	let urlGetHash;
	if (url.split('?').length == 1) {
		urlGetHash = `${url}?get_hash=true`;
	}
	else {
		urlGetHash = `${url}&get_hash=true`;
	}
	const requestMd5 = await fetch(urlGetHash);
	const md5 = (await requestMd5.json())["md5"];
	let storageValue = JSON.parse(sessionStorage.getItem(storageKey));
	if ((storageValue === null) || (storageValue["md5"] !== md5)) {
		const request = await fetch(url);
		storageValue = {"md5": md5, "json": await request.json()};
		sessionStorage.setItem(storageKey, JSON.stringify(storageValue));
	}
	return storageValue["json"];
}

async function getPageData(pageId) {
	json = await getJson(`?page=${pageId}&is_ajax=true`, `md5_${pageId}`);
	return json;
}

const pageNow = () => {
	let url = decodeURI(document.URL.split('=')[1]);
	return (url !== "undefined") ? url : 1;
}

async function ajaxUpdatePage(event) {
	let pageId = event.target.href.split('=')[1];
	if ((pageNow() === `?page=${pageId}`) || (!$("#ajax_checkbox").checked))
		return;

	event.preventDefault();

	let data = await getPageData(pageId);
	changeSiteContent(data);
	window.history.pushState(pageId, data["title"], `?page=${pageId}`);
}

window.addEventListener('popstate', async (e) => changeSiteContent(await getPageData(e.state ? e.state : "1")));

async function logout() {
	let request = await fetch(`/logout/?page=${pageNow()}`);
	window.location.reload();
}

(async () => {
	let data = await getPageData(pageNow());
	changeSiteContent(data);
})()

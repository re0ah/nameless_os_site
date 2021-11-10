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
	$("#content").innerHTML = data["html"];
	$("#content_header").innerHTML = document.title = data["title"];
	$("#content_list").innerHTML = data["content_list"];
	addScript(data["js_url"]);
	addStyle(data["css_url"]);
}

async function checkAuthorization() {
	const request = await fetch("/check_authorization/");
	return await request.status;
}

async function getPageData(pageId) {
	const request_md5 = await fetch(`?page=${pageId}&is_ajax=true&get_hash=true`);
	const md5 = (await request_md5.json())["md5"];
	const storageKey = `md5_${pageId}`;
	let storageValue = JSON.parse(sessionStorage.getItem(storageKey));
	if ((storageValue === null) || (storageValue["md5"] !== md5)) {
		const request = await fetch(`?page=${pageId}&is_ajax=true`);
		storageValue = {"md5": md5, "json": await request.json()};
		sessionStorage.setItem(storageKey, JSON.stringify(storageValue));
	}
	return storageValue["json"];
}

const pageNow = () => {
	let url = decodeURI(document.URL.split('=')[1]);
	return (url !== "undefined") ? url : 1;
}

async function ajaxUpdatePage(event) {
	let pageId = event.target.href.split('=')[1]
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

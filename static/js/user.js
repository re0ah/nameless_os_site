function windowResize() {
	$("#content_wrap").style.maxHeight = (window.innerHeight - 100) + "px";
	$("#content").style.maxHeight = (window.innerHeight - 170) + "px";
};

window.addEventListener('resize', windowResize);
windowResize();

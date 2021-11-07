function windowResize() {
	$("#content_wrap").style.maxHeight = (window.innerHeight - 70) + "px";
	$("#content").style.maxHeight = (window.innerHeight - 140) + "px";
};

window.addEventListener('resize', windowResize);
windowResize();

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

function setCheckboxValue(checkbox, value) {
	if (value === null) {
		value = true;
		document.cookie = `${checkbox.id}=true`;
	}
	else {
		value = value == "true";
	}
	if (checkbox.checked != value) {
		checkbox.click();
	}
}

function initCheckbox(checkboxId, func) {
	let el = $(`#${checkboxId}`);
	setCheckboxValue(el, getCookie(checkboxId));
	el.addEventListener("click", function () {
		document.cookie = `${this.id}=${this.checked}`;
		func();
	})
}

initCheckbox("ajax_checkbox", () => {});

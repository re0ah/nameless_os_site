function sendBugReport() {
        let data = new FormData();
        data.append('title', $("#title_bug_report").value);
        data.append('text', $("#textarea_bug_report").value);
        data.append('csrfmiddlewaretoken', csrftoken);
        fetch("/get_bug_report/", {
                method: 'POST',
                body: data,
                credentials: 'same-origin',
        })
        .then((response) => {
                if(response.status === 200)
                        alert("Сообщение об ошибке передано успешно.")
                else
                        alert("Сообщение передать не удалось.")
        });
}

if (checkAuthorization() === false) {
    $("#notice_bug_report").innerHTML= "Для отправки сообщения о ошибке необходимо быть авторизованным";
}
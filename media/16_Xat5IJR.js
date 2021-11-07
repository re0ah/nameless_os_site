function sendTaskOffer() {
        let data = new FormData();
        data.append('title', $("#title_task_offer").value);
        data.append('text', $("#textarea_task_offer").value);
        data.append('csrfmiddlewaretoken', csrftoken);
        fetch("/get_task_offer/", {
                method: 'POST',
                body: data,
                credentials: 'same-origin',
        })
        .then((response) => {
                if(response.status === 200)
                        alert("Сообщение о предложеной задаче передано успешно.")
                else
                        alert("Сообщение передать не удалось.")
        });
}

if (checkAuthorization() === false) {
    $("#notice_bug_report").innerHTML= "Для отправки предложения задачи необходимо быть авторизованным";
}
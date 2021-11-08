function sendTaskOffer() {
        let data = new FormData();
        data.append('title', document.getElementById("title_task_offer").value);
        data.append('text', document.getElementById("textarea_task_offer").value);
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
    document.getElementById("notice_task_offer").innerHTML= "Для отправки предложения задачи необходимо быть авторизованным";
}
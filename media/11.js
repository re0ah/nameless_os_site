if(true){
var xhr = new XMLHttpRequest();
xhr.open("GET", `/get_task_list_current/`, false);
xhr.send(null);
document.getElementById("wrap_task_tracker_current").innerHTML = JSON.parse(xhr.responseText)["task_list"];
}
if(true){
var xhr = new XMLHttpRequest();
xhr.open("GET", `/get_task_list_solved/`, false);
xhr.send(null);
document.getElementById("wrap_task_tracker_solved").innerHTML = JSON.parse(xhr.responseText)["task_list"];
}
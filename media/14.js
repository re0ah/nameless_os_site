if(true){
var xhr = new XMLHttpRequest();
xhr.open("GET", `/get_bug_list_current/`, false);
xhr.send(null);
document.getElementById("wrap_bug_tracker_current").innerHTML = JSON.parse(xhr.responseText)["bug_list"];
}
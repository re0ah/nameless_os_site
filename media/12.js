(async () => {
$("#wrap_task_tracker_deffered").innerHTML = (await getJson('/get_task_list_deffered/', 'get_task_list_deffered'))["task_list"];
})();
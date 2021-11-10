(async () => {
$("#wrap_task_tracker_current").innerHTML = (await getJson('/get_task_list_current/', 'get_task_list_current'))["task_list"];
})();
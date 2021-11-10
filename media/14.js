(async () => {
$("#wrap_bug_tracker_current").innerHTML = (await getJson('/get_bug_list_current/', 'get_bug_list_current'))["bug_list"];
})();
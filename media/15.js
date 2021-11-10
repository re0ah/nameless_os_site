(async () => {
$("#wrap_bug_tracker_current").innerHTML = (await getJson('/get_bug_list_solved/', 'get_bug_list_solved'))["bug_list"];
})();
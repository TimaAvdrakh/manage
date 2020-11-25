$(document).foundation()


var HOST = "http://127.0.0.1:8011/"

function getFolderList(selector) {
    $.ajax({
        type: "GET",
        url: HOST + "api/folder_task/?format=json",
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function (data) {
            selector.jstree(data);
        },
        error: function (errMsg) {
            alert(errMsg);
        }
    });
}
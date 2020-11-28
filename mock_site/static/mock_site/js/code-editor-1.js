$(document).on("click", '#download_code', function (e) {
    function saveFile(name, type, data) {
        if (data !== null && navigator.msSaveBlob)
            return navigator.msSaveBlob(new Blob([data], {type: type}), name);
        var a = $("<a style='display: none;'/>");
        var url = window.URL.createObjectURL(new Blob([data], {type: type}));
        a.attr("href", url);
        a.attr("download", name);
        $("body").append(a);
        a[0].click();
        window.URL.revokeObjectURL(url);
        a.remove();
    }

    var selectDD = document.getElementById("slct");
    var language = selectDD.value;
    var fileType = 'txt';
    if (language === 'python') {
        fileType = 'py';
    } else if (language === 'ruby') {
        fileType = 'rb';
    } else if (language === 'cpp') {
        fileType = 'cpp';
    } else if (language === 'c') {
        fileType = 'c';
    } else {
        fileType = 'txt';
    }

    let fileName = 'code.' + fileType;
    let txt = $('#script_text_area').val();
    saveFile(fileName, "data:attachment/text", txt);
});


$(document).on("click", '#reset_code', function (e) {
    document.getElementById("script_text_area").value = "";
    $("#script_result").val('');

});
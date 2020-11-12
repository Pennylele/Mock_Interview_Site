$(document).on("click", '#run_python_script', function (e) {
    let txt = $('#script_text_area').val();
    console.log(txt);

    var e = document.getElementById("slct");
    let language = e.options[e.selectedIndex].value;
    $.ajax({
        url: "{% url 'result' %}",
        type: "POST",
        data: {
            'script': txt,
            'language': language,
            csrfmiddlewaretoken: '{{ csrf_token }}',
        },
        dataType: 'json',
        success: function (data) {
            console.log(data);
            $("#script_result").val(data["output"]);
        },
        error: function (data) {
            console.log("error");
            console.log(data);
        }
    });
});

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
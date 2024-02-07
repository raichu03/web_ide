let editor;
let language;
let code;

window.onload = function () {
    editor = ace.edit("editor");
    editor.setTheme("ace/theme/twilight");
    editor.session.setMode("ace/mode/python");
    language = 'py';
};

function setLang(lang){
    switch(lang){
        case 'c':
            editor.session.setMode("ace/mode/c_cpp");
            break;
        case 'cpp':
            editor.session.setMode("ace/mode/c_cpp");
            break;
        case 'py':
            editor.session.setMode("ace/mode/python");
            break;
        case 'php':
            editor.session.setMode("ace/mode/php");
            break;
        case 'js':
            editor.session.setMode("ace/mode/javascript");
            break;
    }
}

function executeCode(){
    var jsonData = {
        code : editor.getSession().getValue(),
        language : language
    };

    $.ajax({
        url: "http://127.0.0.1:8000/compile-code",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify(jsonData),
        success: function (data){
            // var formatteddata = data.replace(/\n/g,"<br>");
            // $(".question-box").html(formatteddata);
            console.log(data);
        }
    })
    
}
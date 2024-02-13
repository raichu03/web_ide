let editor;
let language;
let code;

// const serverUrl = "http://127.0.0.1:8000"

window.onload = function () {
    editor = ace.edit("editor");
    editor.setTheme("ace/theme/twilight");
    editor.session.setMode("ace/mode/python");
    language = 'py';
};


document.querySelector("#difficulty").addEventListener("change", function(){
    difficulty = this.value;
    
    $.ajax({
        url: "http://127.0.0.1:8000/questions",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify({difficulty: difficulty}),
        success: function (data){
            console.log(data["title"]);
            $(".question-title").html(data["title"]);
            $(".question-discription").html(data["description"]);
            $(".example-1").html(data["example-1"]);
            $(".example-2").html(data["example-2"]);
        }
    })
});

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
            var formatteddata = data.replace(/\n/g,"<br>");
            $(".display-output").html(formatteddata);
            
        }
    })
    
}
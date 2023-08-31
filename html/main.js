
let editor;

window.onload = function () {
  editor = ace.edit("editor");
  editor.setTheme("ace/theme/cobalt");
};

var language_data;

function changeLanguage(language) {
  language_data = language;
  if (language == 'c') editor.session.setMode("ace/mode/c_cpp");
  else if (language == 'cpp') editor.session.setMode("ace/mode/c_cpp");
  else if (language == 'py') editor.session.setMode("ace/mode/python");
  else if (language == 'php') editor.session.setMode("ace/mode/php");
  else if (language == 'js') editor.session.setMode("ace/mode/javascript");
};


function changeDifficulty(){
  const difficultyMode = document.getElementById('modeSelect');
  let hasSelected = false;
  const mode = difficultyMode.value;
  var myData = {
    difficulty: mode
  }

  if (!hasSelected) {
    hasSelected = true;
    difficultyMode.disabled = true;
  };


  $.ajax({
    url: "http://127.0.0.1:8000/question",
    type: "POST",
    contentType: "application/json",
    data: JSON.stringify(myData),
    success: function (data) {
      var formattedData = "Q. " + data.id +": &emsp;"+ data.title + "<br><br><br>&emsp;" + data.description + "<br><br><br>&emsp;" + data.example;
      console.log(formattedData);
      $(".questions").html(formattedData);
    }
  });


};


function executeCode() {
  var jsonData = {
    language: language_data,
    code: editor.getSession().getValue()
  };

  $.ajax({
    url: "http://127.0.0.1:8000/compile",
    type: "POST",
    contentType: "application/json",
    data: JSON.stringify(jsonData),
    success: function (data) {
      var formatteddata = data.replace(/\n/g,"<br>");
      $(".output").html(formatteddata);
    }
  });
};
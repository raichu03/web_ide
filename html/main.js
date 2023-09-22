let editor;
let hasSelected = false; // Initialize hasSelected here

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
  
  startTimer()
  const difficultyMode = document.getElementById('modeSelect');
  
  const mode = difficultyMode.value;
  console.log(mode)
  switch(mode){
    case "easy":
      startTimer(120)
      break;
    case "medium":
      startTimer(300)
      break;
    case "hard":
      startTimer(600)
      break;
  }
    

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

var timerInterval;
var timerSeconds;

function startTimer(durationInSeconds) {
  clearInterval(timerInterval); 
  
  timerSeconds = durationInSeconds;
  
  timerInterval = setInterval(function () {
    timerSeconds--;
    if (timerSeconds < 0) {
      clearInterval(timerInterval);
      document.getElementById('timerDisplay').textContent = 'Timer: 0 seconds';
      
      window.location.href = 'index.html';
    } else {
      document.getElementById('timerDisplay').textContent =  timerSeconds ;
    }
  }, 1000); // Update every 1000 milliseconds (1 second)
}



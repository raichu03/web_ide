require.config({ 
    paths: { 
        'vs': 'https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.45.0/min/vs'
    } 
});

var editor;
var language = 'python';

require(['vs/editor/editor.main'], function () {
    editor = monaco.editor.create(document.getElementById('editor'), {
        language: language,
        theme: 'vs-dark',
        fontSize: 22,
        minimap: {
            enabled: true
        },
        lineNumbers: 'on',
        wordWrap: 'on',
        automaticLayout: true,
    });
});

function changeLanguage() {
    language = document.getElementById('languages').value;
    monaco.editor.setModelLanguage(editor.getModel(), language);
}

function setOutput(output){
    document.getElementById('output-box').textContent = output;
}

function runCode() {
    const code = editor.getValue();
    fetch('/execute',{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({code, language})
    })
    .then(response => response.json())
    .then(data => {
        if(data['return_code'] === 0){
            setOutput(data['stdout']);
        } else {
            setOutput(data['stderr']);
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}
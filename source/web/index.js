require.config({ 
    paths: { 
        'vs': 'https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.45.0/min/vs'
    } 
});

var editor;

require(['vs/editor/editor.main'], function () {
    editor = monaco.editor.create(document.getElementById('editor'), {
        language: 'javascript',
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
    const language = document.getElementById('languages').value;
    monaco.editor.setModelLanguage(editor.getModel(), language);
}
require.config({ 
    paths: { 
        'vs': 'https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.45.0/min/vs'
    } 
});

require(['vs/editor/editor.main'], function () {
    monaco.editor.create(document.getElementById('editor'), {
        // value: `function hello() {\n console.log('Hello world!')\n}`,
        language: 'javascript',
        theme: 'vs-dark'
    });
});
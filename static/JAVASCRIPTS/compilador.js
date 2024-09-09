document.addEventListener("DOMContentLoaded", function () {
    var sqlEditor = CodeMirror.fromTextArea(
        document.getElementById("sql-editor"),
        {
            mode: "text/x-sql",
            theme: "dracula",
            lineNumbers: true,
            lineWrapping: true,
            readOnly: false,
            matchBrackets: true,
            autoCloseBrackets: true,
            autoCloseTags: true,
            indentUnit: 2,
            tabSize: 2,
            smartIndent: true,
            showCursorWhenSelecting: true,
            viewportMargin: Infinity,
            foldGutter: true
        }
    );
});
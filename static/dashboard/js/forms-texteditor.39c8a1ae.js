"use strict";
document.addEventListener("DOMContentLoaded", (function() {
    new Quill("#editor", {
        modules: {
            toolbar: [
                ["bold", "italic", "underline", "strike"],
                [{
                    header: 1
                }, {
                    header: 2
                }],
                [{
                    list: "ordered"
                }, {
                    list: "bullet"
                }],
                [{
                    indent: "-1"
                }, {
                    indent: "+1"
                }],
                [{
                    direction: "rtl"
                }],
                [{
                    size: ["small", !1, "large", "huge"]
                }],
                [{
                    header: [1, 2, 3, 4, 5, 6, !1]
                }],
                [{
                    color: []
                }, {
                    background: []
                }],
                [{
                    font: []
                }],
                [{
                    align: []
                }],
                ["clean"]
            ]
        },
        placeholder: "Compose an epic...",
        theme: "snow"
    })
}));
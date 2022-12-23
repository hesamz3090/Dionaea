"use strict";
document.addEventListener("DOMContentLoaded", (function() {
    function e(e, r) {
        e.forEach((e => {
            e.classList.contains("js-validate-error-field") ? (e.classList.add("is-invalid"), e.classList.remove("is-valid")) : (e.classList.remove("is-invalid"), e.classList.add("is-valid"))
        }))
    }
    new window.JustValidate("#simpleLoginForm", {
        rules: {
            email: {
                required: !0,
                email: !0
            },
            password: {
                required: !0
            }
        },
        messages: {
            email: "Please enter a valid email",
            password: "Please enter your password"
        },
        invalidFormCallback: function() {
            let r = document.querySelectorAll("#simpleLoginForm input[required]"),
                i = document.querySelector("#simpleLoginForm");
            e(r), i.addEventListener("keyup", (() => e(r)))
        }
    }), new window.JustValidate("#editorForm", {
        rules: {
            editorName: {
                required: !0
            },
            editorContent: {
                required: !0
            }
        },
        messages: {
            editorName: "Name is required",
            editorContent: "Please write something :)"
        },
        invalidFormCallback: function() {
            let r = document.querySelectorAll("#editorForm [required]"),
                i = document.querySelector("#editorForm");
            e(r), i.addEventListener("keyup", (() => e(r)))
        }
    });
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
    });
    new window.JustValidate("#form2", {
        rules: {
            email: {
                required: !0,
                email: !0
            },
            name: {
                required: !0
            },
            password: {
                required: !0,
                minLength: 5
            },
            passwordConfirmation: {
                required: !0,
                function: (e, r) => r == document.getElementById("password").value
            }
        },
        messages: {
            name: "Please enter a your name",
            email: "Please enter a valid email",
            password: "Please enter your password",
            passwordConfirmation: "password doesnt match"
        },
        invalidFormCallback: function() {
            let r = document.querySelectorAll("#form2 input[required]"),
                i = document.querySelector("#form2");
            e(r), i.addEventListener("keyup", (() => e(r)))
        }
    })
}));
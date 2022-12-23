"use strict";
document.addEventListener("DOMContentLoaded", (function() {
    let e = document.querySelectorAll("input.input-material");
    document.querySelectorAll("label.label-material");

    function t() {
        var e = document.querySelector("#footer").outerHeight;
        o.style.paddingBottom = `${e}px`
    }
    Array.from(e).filter((function(e) {
        return "" !== e.value
    })).forEach((e => e.parentElement.lastElementChild.setAttribute("class", "label-material active"))), e.forEach((e => {
        e.addEventListener("focus", (function() {
            e.parentElement.lastElementChild.setAttribute("class", "label-material active")
        }))
    })), e.forEach((e => {
        e.addEventListener("blur", (function() {
            "" !== e.value ? e.parentElement.lastElementChild.setAttribute("class", "label-material active") : e.parentElement.lastElementChild.setAttribute("class", "label-material")
        }))
    })), document.querySelector("#footer") && (document.addEventListener("sidebarChanged", (function() {
        t()
    })), window.addEventListener("resize", (function() {
        t()
    })));
    document.querySelectorAll(".card-close a.remove").forEach((e => {
        e.addEventListener("click", (t => {
            t.preventDefault(), e.closest(".card").style.opacity = "0", setTimeout((function() {
                e.closest(".card").classList.add("d-none")
            }), 300)
        }))
    }));
    const r = document.querySelectorAll(".card-close .dropdown-toggle");
    r.forEach((e => {
        e.addEventListener("click", (() => {
            e.classList.contains("show") && setTimeout((function() {
                e.nextElementSibling.classList.add("is-visible")
            }), 100)
        }))
    })), document.addEventListener("click", (function(e) {
        r.forEach((t => {
            e.target == t ? setTimeout((function() {
                t.nextElementSibling.classList.add("is-visible")
            }), 100) : t.nextElementSibling.classList.remove("is-visible")
        }))
    }));
    var n = document.querySelector(".search-open"),
        l = document.querySelector(".search-dashboard"),
        s = document.querySelector(".search-dashboard .close-btn");
    n && (n.addEventListener("click", (function(e) {
        e.preventDefault(), l.style.display = "block"
    })), s.addEventListener("click", (function(e) {
        e.preventDefault(), l.style.display = "none"
    })));
    [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]')).map((function(e) {
        return new bootstrap.Tooltip(e)
    }));
    var i = document.querySelector(".sidebar-toggle"),
        a = document.querySelector("#sidebar"),
        o = document.querySelector(".page-content"),
        c = document.querySelector(".navbar-brand");

    function d(e, t) {
        e.forEach((e => {
            e.classList.contains("js-validate-error-field") ? (e.classList.add("is-invalid"), e.classList.remove("is-valid")) : (e.classList.remove("is-invalid"), e.classList.add("is-valid"))
        }))
    }
    i && i.addEventListener("click", (function() {
        this.classList.toggle("active"), c.classList.toggle("active"), a.classList.toggle("shrinked"), o.classList.toggle("active"), document.dispatchEvent(new Event("sidebarChanged"))
    }));
    let u = document.querySelector(".login-form");
    u && new window.JustValidate(".login-form", {
        rules: {
            loginUsername: {
                required: !0,
                email: !0
            },
            loginPassword: {
                required: !0
            }
        },
        messages: {
            loginUsername: "Please enter a valid email",
            loginPassword: "Please enter your password"
        },
        invalidFormCallback: function() {
            let e = document.querySelectorAll(".login-form input[required]");
            d(e), u.addEventListener("keyup", (() => d(e)))
        }
    });
    let m = document.querySelector(".register-form");
    m && new window.JustValidate(".register-form", {
        rules: {
            registerUsername: {
                required: !0
            },
            registerEmail: {
                required: !0,
                email: !0
            },
            registerPassword: {
                required: !0
            },
            registerAgree: {
                required: !0
            }
        },
        messages: {
            registerUsername: "Please enter your username",
            registerEmail: "Please enter a valid email address",
            registerPassword: "Please enter your password",
            registerAgree: "Your agreement is required"
        },
        invalidFormCallback: function() {
            let e = document.querySelectorAll(".register-form input[required]");
            d(e), m.addEventListener("keyup", (() => d(e))), m.addEventListener("change", (() => d(e)))
        }
    });
    const g = document.querySelector(".profile-country-choices");
    if (g) {
        new Choices(g, {
            searchEnabled: !1,
            placeholder: !1,
            callbackOnInit: () => function(e) {
                let t = e.dataset.customclass.split(" ");
                e.parentElement.classList.add.apply(e.parentElement.classList, t)
            }(g)
        })
    }
    const v = document.querySelector(".msnry-grid");
    if (v) {
        var f = new Masonry(v, {
            percentPosition: !0
        });
        imagesLoaded(v).on("progress", (function() {
            f.layout()
        }))
    }
}));
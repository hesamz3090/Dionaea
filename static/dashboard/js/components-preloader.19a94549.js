"use strict";

function hidePreloader() {
    let e = document.querySelector(".spinner-wrapper");
    setTimeout((function() {
        e.style.opacity = "0"
    }), 1e3), setTimeout((function() {
        e.remove()
    }), 1500)
}
window.addEventListener("load", (function() {
    hidePreloader()
}));
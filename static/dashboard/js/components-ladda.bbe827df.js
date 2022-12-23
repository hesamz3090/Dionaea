"use strict";
document.addEventListener("DOMContentLoaded", (function() {
    Ladda.bind(".ladda-button:not(.ladda-button-progress)", {
        timeout: 2e3
    }), Ladda.bind(".ladda-button-progress", {
        callback: function(t) {
            var a = 0,
                n = setInterval((function() {
                    a = Math.min(a + .1 * Math.random(), 1), t.setProgress(a), 1 === a && (t.stop(), clearInterval(n))
                }), 200)
        }
    })
}));
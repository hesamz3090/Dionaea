"use strict";
document.addEventListener("DOMContentLoaded", (function() {
    var e = document.getElementById("gauge1"),
        t = document.getElementById("gauge2"),
        a = document.getElementById("gauge3"),
        n = document.getElementById("gauge4"),
        o = {
            angle: 0,
            lineWidth: .06,
            radiusScale: 1,
            pointer: {
                length: .6,
                strokeWidth: .035,
                color: "#fff"
            },
            fontSize: 20,
            limitMax: !1,
            limitMin: !1,
            colorStart: "#6F6EA0",
            colorStop: "#C0C0DB",
            strokeColor: "#eee",
            generateGradient: !1,
            scaleOverride: !0,
            highDpiSupport: !0
        };
    o.colorStop = "#864DD9";
    var l = new Donut(e).setOptions(o);
    l.maxValue = 3e3, l.setMinValue(0), l.set(Math.floor(3e3 * Math.random())), l.setTextField(document.getElementById("gauge1Value")), o.colorStop = "#CF53F9";
    var r = new Donut(t).setOptions(o);
    r.maxValue = 3e3, r.setMinValue(0), r.set(Math.floor(3e3 * Math.random())), r.setTextField(document.getElementById("gauge2Value")), o.colorStop = "#e95f71";
    var u = new Donut(a).setOptions(o);
    u.maxValue = 3e3, u.setMinValue(0), u.set(Math.floor(3e3 * Math.random())), u.setTextField(document.getElementById("gauge3Value")), o.colorStop = "#7127AC";
    var i = new Donut(n).setOptions(o);
    i.maxValue = 3e3, i.setMinValue(0), i.set(Math.floor(3e3 * Math.random())), i.setTextField(document.getElementById("gauge4Value"));
    setInterval((function() {
        l.set(Math.floor(3e3 * Math.random())), r.set(Math.floor(3e3 * Math.random())), u.set(Math.floor(3e3 * Math.random())), i.set(Math.floor(3e3 * Math.random()))
    }), 5e3);

    function m(e, t) {
        if (e.tagName === t) return e;
        for (;
            (e = e.parentNode) && e.tagName !== t;);
        return e
    }
    var d = {
        onmousemove(e, t) {
            var a = m(e.target, "svg").nextElementSibling,
                n = new Date(t.date).toUTCString().replace(/^.*?, (.*?) \d{2}:\d{2}:\d{2}.*?$/, "$1");
            a.hidden = !1, a.textContent = `${n}: $${t.value.toFixed(2)} USD`, a.style.top = `${e.offsetY}px`, a.style.left = `${e.offsetX+20}px`
        },
        onmouseout() {
            m(event.target, "svg").nextElementSibling.hidden = !0
        }
    };

    function s() {
        for (var e = [], t = 0; t < 20; t += 1) e.push(50 * Math.random());
        return e
    }
    sparkline.sparkline(document.querySelector(".btc"), [{
        name: "Bitcoin",
        date: "2017-01-01",
        value: 967.6
    }, {
        name: "Bitcoin",
        date: "2017-02-01",
        value: 957.02
    }, {
        name: "Bitcoin",
        date: "2017-03-01",
        value: 1190.78
    }, {
        name: "Bitcoin",
        date: "2017-04-01",
        value: 1071.48
    }, {
        name: "Bitcoin",
        date: "2017-05-01",
        value: 1354.21
    }, {
        name: "Bitcoin",
        date: "2017-06-01",
        value: 2308.08
    }, {
        name: "Bitcoin",
        date: "2017-07-01",
        value: 2483.5
    }, {
        name: "Bitcoin",
        date: "2017-08-01",
        value: 2839.18
    }, {
        name: "Bitcoin",
        date: "2017-09-01",
        value: 4744.69
    }, {
        name: "Bitcoin",
        date: "2017-10-01",
        value: 4348.09
    }, {
        name: "Bitcoin",
        date: "2017-11-01",
        value: 6404.92
    }], d), sparkline.sparkline(document.querySelector(".eth"), [{
        name: "Ethereum",
        date: "2017-01-01",
        value: 8.3
    }, {
        name: "Ethereum",
        date: "2017-02-01",
        value: 10.57
    }, {
        name: "Ethereum",
        date: "2017-03-01",
        value: 15.73
    }, {
        name: "Ethereum",
        date: "2017-04-01",
        value: 49.51
    }, {
        name: "Ethereum",
        date: "2017-05-01",
        value: 85.69
    }, {
        name: "Ethereum",
        date: "2017-06-01",
        value: 226.51
    }, {
        name: "Ethereum",
        date: "2017-07-01",
        value: 246.65
    }, {
        name: "Ethereum",
        date: "2017-08-01",
        value: 213.87
    }, {
        name: "Ethereum",
        date: "2017-09-01",
        value: 386.61
    }, {
        name: "Ethereum",
        date: "2017-10-01",
        value: 303.56
    }, {
        name: "Ethereum",
        date: "2017-11-01",
        value: 298.21
    }], d), document.querySelectorAll(".sparkline-static").forEach((function(e) {
        sparkline.sparkline(e, s())
    })), setInterval((function() {
        document.querySelectorAll(".sparkline-random").forEach((function(e) {
            sparkline.sparkline(e, s())
        }))
    }), 3e3)
}));
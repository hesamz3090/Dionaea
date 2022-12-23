"use strict";
document.addEventListener("DOMContentLoaded", (function() {
    var e = document.getElementById("basicNoUISlider");
    e && noUiSlider.create(e, {
        start: [20, 80],
        range: {
            min: [0],
            max: [100]
        }
    });
    var t = document.getElementById("stepNoUISlider");
    t && noUiSlider.create(t, {
        start: [200, 1e3],
        range: {
            min: [0],
            max: [1800]
        },
        step: 100,
        tooltips: !0,
        connect: !0
    });
    new Datepicker(document.querySelector(".input-datepicker"), {
        buttonClass: "btn",
        format: "mm/dd/yyyy"
    }), new Datepicker(document.querySelector(".input-datepicker-autoclose"), {
        buttonClass: "btn",
        autohide: !0
    }), new Datepicker(document.querySelector(".input-datepicker-multiple"), {
        buttonClass: "btn",
        maxNumberOfDates: 3
    });
    var n;
    if (n = document.getElementById("isbn1")) {
        var a = {
            mask: "000-00-000-0000-0"
        };
        IMask(n, a)
    }
    if (n = document.getElementById("isbn2")) a = {
        mask: "000 00 000 0000 0"
    }, IMask(n, a);
    if (n = document.getElementById("isbn3")) a = {
        mask: "000/00/000/0000/0"
    }, IMask(n, a);
    if (n = document.getElementById("ip4")) a = {
        mask: "000.000.000.000'"
    }, IMask(n, a);
    if (n = document.getElementById("currency")) a = {
        mask: "$ num",
        blocks: {
            num: {
                mask: Number,
                thousandsSeparator: ",",
                radix: "."
            }
        }
    }, IMask(n, a);
    if (n = document.getElementById("date")) a = {
        mask: Date,
        pattern: "Y-m-d",
        blocks: {
            d: {
                mask: IMask.MaskedRange,
                from: 1,
                to: 31,
                maxLength: 2
            },
            m: {
                mask: IMask.MaskedRange,
                from: 1,
                to: 12,
                maxLength: 2
            },
            Y: {
                mask: IMask.MaskedRange,
                from: 1900,
                to: 9999
            }
        },
        format: function(e) {
            var t = e.getDate(),
                n = e.getMonth() + 1;
            return t < 10 && (t = "0" + t), n < 10 && (n = "0" + n), [e.getFullYear(), n, t].join("-")
        },
        parse: function(e) {
            var t = e.split("-");
            return new Date(t[0], t[1] - 1, t[2])
        }
    }, IMask(n, a);
    if (n = document.getElementById("phone")) a = {
        mask: "+{1}-000-000-0000"
    }, IMask(n, a);
    if (n = document.getElementById("taxId")) a = {
        mask: "00-000000"
    }, IMask(n, a);
    var c = document.getElementById("multiselect1");

    function o(e) {
        let t = e.dataset.customclass.split(" ");
        e.parentElement.classList.add.apply(e.parentElement.classList, t)
    }
    multi(c);
    const s = document.querySelector(".choices-primary"),
        r = (new Choices(s, {
            searchEnabled: !1,
            callbackOnInit: () => o(s)
        }), document.querySelector(".choices-secondary")),
        m = (new Choices(r, {
            searchEnabled: !1,
            callbackOnInit: () => o(r)
        }), document.querySelector(".choices-outlined")),
        l = (new Choices(m, {
            searchEnabled: !1,
            placeholder: !0,
            removeItemButton: !0,
            placeholderValue: "Choose your country",
            callbackOnInit: () => o(m)
        }), document.querySelector(".tags-input")),
        d = (new Choices(l, {
            searchEnabled: !1,
            removeItemButton: !0,
            callbackOnInit: () => o(l)
        }), document.querySelector(".tags-email")),
        i = (new Choices(d, {
            callbackOnInit: () => o(d),
            addItemFilter: function(e) {
                if (!e) return !1;
                return new RegExp(/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.source, "i").test(e)
            }
        }), document.querySelector(".tags-disabled"));
    new Choices(i, {
        searchEnabled: !1,
        removeItemButton: !0,
        callbackOnInit: () => o(i)
    }).disable()
}));
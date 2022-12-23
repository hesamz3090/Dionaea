"use strict";
document.addEventListener("DOMContentLoaded", (function() {
    const e = document.getElementById("autoComplete1"),
        t = new autoComplete({
            selector: "#autoComplete1",
            data: {
                src: e.dataset.source.split(",")
            },
            resultItem: {
                highlight: !0
            },
            events: {
                input: {
                    selection: e => {
                        const a = e.detail.selection.value;
                        t.input.value = a
                    }
                }
            }
        }),
        a = new autoComplete({
            selector: "#autoComplete2",
            data: {
                src: ["Sauce", "Wild Boar", "Goat"]
            },
            resultItem: {
                highlight: !0
            },
            events: {
                input: {
                    selection: e => {
                        const t = e.detail.selection.value;
                        a.input.value = t
                    }
                }
            }
        }),
        n = new autoComplete({
            selector: "#autoComplete3",
            data: {
                src: async () => {
                    try {
                        const e = await fetch("data/countries.07cc3b94.json");
                        return (await e.json()).countries
                    } catch (e) {
                        return e
                    }
                }
            },
            resultItem: {
                highlight: !0
            },
            events: {
                input: {
                    selection: e => {
                        const t = e.detail.selection.value;
                        n.input.value = t
                    }
                }
            }
        }),
        o = new autoComplete({
            selector: "#autoComplete4",
            data: {
                src: [{
                    name: "Alyce",
                    surname: "White",
                    company: "Combot",
                    email: "alycewhite@combot.com",
                    city: "Talpa"
                }, {
                    name: "Santos",
                    surname: "Pierce",
                    company: "Franscene",
                    email: "santospierce@franscene.com",
                    city: "Vienna"
                }, {
                    name: "Deirdre",
                    surname: "Reed",
                    company: "Whiskey Comp.",
                    email: "deirdrereed@whiskeycomp.com",
                    city: "Belva"
                }, {
                    name: "Whitaker",
                    surname: "Brennan",
                    company: "Opticom",
                    email: "whitakerbrennan@opticom.com",
                    city: "Lodoga"
                }, {
                    name: "Kristin",
                    surname: "Norman",
                    company: "Irack",
                    email: "kristinnorman@irack.com",
                    city: "Bodega"
                }],
                keys: ["name", "surname", "company"]
            },
            resultItem: {
                highlight: !0
            },
            events: {
                input: {
                    selection: e => {
                        const t = e.detail.selection.value;
                        o.input.value = t.email
                    }
                }
            }
        })
}));
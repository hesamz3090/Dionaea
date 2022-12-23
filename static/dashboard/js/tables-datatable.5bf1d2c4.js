"use strict";
document.addEventListener("DOMContentLoaded", (function() {
    const e = new simpleDatatables.DataTable("#datatable1", {
        searchable: !1,
        labels: {
            perPage: "Show {select} entries",
            info: "Showing {start} to {end} of {rows} entries"
        }
    });

    function t() {
        let t = e.columns();
        window.innerWidth > 900 ? t.show([2, 3, 4, 5]) : window.innerWidth > 600 ? (t.hide([4, 5]), t.show([2, 3])) : t.hide([2, 3, 4, 5])
    }
    t(), window.addEventListener("resize", t), e.on("datatable.init", (function() {
        ! function(e) {
            const t = e.table.closest(".dataTable-wrapper"),
                a = t.querySelector(".dataTable-input");
            a && a.classList.add("form-control", "form-control-sm");
            const n = t.querySelector(".dataTable-selector");
            n && n.classList.add("form-select", "form-select-sm");
            const o = t.querySelector(".dataTable-container");
            o && o.classList.add("border-0")
        }(e)
    }))
}));
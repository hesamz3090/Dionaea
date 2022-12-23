"use strict";
Dropzone.options.demoUpload = !1, document.addEventListener("DOMContentLoaded", (function() {
    var e = new Dropzone("#demo-upload", {
        parallelUploads: 2,
        thumbnailHeight: 120,
        thumbnailWidth: 120,
        maxFilesize: 3,
        filesizeBase: 1e3,
        thumbnail: function(e, t) {
            if (e.previewElement) {
                e.previewElement.classList.remove("dz-file-preview");
                for (var o = e.previewElement.querySelectorAll("[data-dz-thumbnail]"), s = 0; s < o.length; s++) {
                    var i = o[s];
                    i.alt = e.name, i.src = t
                }
                setTimeout((function() {
                    e.previewElement.classList.add("dz-image-preview")
                }), 1)
            }
        }
    });
    e.uploadFiles = function(e) {
        for (var t = this, o = 0; o < e.length; o++)
            for (var s = e[o], i = Math.round(Math.min(60, Math.max(6, s.size / 1e5))), a = 0; a < i; a++) {
                var n = 100 * (a + 1);
                setTimeout(function(e, o, s) {
                    return function() {
                        e.upload = {
                            progress: 100 * (s + 1) / o,
                            total: e.size,
                            bytesSent: (s + 1) * e.size / o
                        }, t.emit("uploadprogress", e, e.upload.progress, e.upload.bytesSent), 100 == e.upload.progress && (e.status = Dropzone.SUCCESS, t.emit("success", e, "success", null), t.emit("complete", e), t.processQueue())
                    }
                }(s, i, a), n)
            }
    }
}));
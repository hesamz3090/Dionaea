"use strict";
document.addEventListener("DOMContentLoaded", (function() {
    Chart.defaults.global.defaultFontColor = "#75787c";
    const o = document.getElementById("lineChartCustom1"),
        r = document.getElementById("barChartCustom1"),
        e = document.getElementById("barChartCustom2"),
        a = document.getElementById("lineChartCustom2"),
        t = document.getElementById("lineChartCustom3"),
        d = document.getElementById("barChartCustom3"),
        n = document.getElementById("pieChartCustom1"),
        i = document.getElementById("doughnutChartCustom1"),
        l = document.getElementById("polarChartCustom"),
        s = document.getElementById("radarChartCustom");
    new Chart(o, {
        type: "line",
        options: {
            legend: {
                labels: {
                    fontColor: "#777",
                    fontSize: 12
                }
            },
            scales: {
                xAxes: [{
                    display: !1,
                    gridLines: {
                        color: "transparent"
                    }
                }],
                yAxes: [{
                    ticks: {
                        max: 60,
                        min: 0
                    },
                    display: !0,
                    gridLines: {
                        color: "transparent"
                    }
                }]
            }
        },
        data: {
            labels: ["January", "February", "March", "April", "May", "June", "July"],
            datasets: [{
                label: "Data Set One",
                fill: !0,
                lineTension: 0,
                backgroundColor: "rgba(134, 77, 217, 0.88)",
                borderColor: "rgba(134, 77, 217, 088)",
                borderCapStyle: "butt",
                borderDash: [],
                borderDashOffset: 0,
                borderJoinStyle: "miter",
                borderWidth: 1,
                pointBorderColor: "rgba(134, 77, 217, 0.88)",
                pointBackgroundColor: "#fff",
                pointBorderWidth: 1,
                pointHoverRadius: 5,
                pointHoverBackgroundColor: "rgba(134, 77, 217, 0.88)",
                pointHoverBorderColor: "rgba(134, 77, 217, 0.88)",
                pointHoverBorderWidth: 2,
                pointRadius: 1,
                pointHitRadius: 10,
                data: [0, 20, 17, 40, 30, 22, 30],
                spanGaps: !1
            }, {
                label: "Data Set Two",
                fill: !0,
                lineTension: 0,
                backgroundColor: "rgba(98, 98, 98, 0.5)",
                borderColor: "rgba(98, 98, 98, 0.5)",
                borderCapStyle: "butt",
                borderDash: [],
                borderDashOffset: 0,
                borderJoinStyle: "miter",
                borderWidth: 1,
                pointBorderColor: "rgba(98, 98, 98, 0.5)",
                pointBackgroundColor: "#fff",
                pointBorderWidth: 1,
                pointHoverRadius: 5,
                pointHoverBackgroundColor: "rgba(98, 98, 98, 0.5)",
                pointHoverBorderColor: "rgba(98, 98, 98, 0.5)",
                pointHoverBorderWidth: 2,
                pointRadius: 1,
                pointHitRadius: 10,
                data: [0, 30, 22, 20, 35, 25, 50],
                spanGaps: !1
            }]
        }
    }), new Chart(r, {
        type: "bar",
        options: {
            scales: {
                xAxes: [{
                    display: !0,
                    barPercentage: .2
                }],
                yAxes: [{
                    ticks: {
                        max: 100,
                        min: 0
                    },
                    display: !1
                }]
            },
            legend: {
                display: !1
            }
        },
        data: {
            labels: ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"],
            datasets: [{
                label: "Data Set 1",
                backgroundColor: ["#EF8C99", "#EF8C99", "#EF8C99", "#EF8C99", "#EF8C99", "#EF8C99", "#EF8C99", "#EF8C99", "#EF8C99", "#EF8C99", "#EF8C99", "#EF8C99"],
                borderColor: ["#EF8C99", "#EF8C99", "#EF8C99", "#EF8C99", "#EF8C99", "#EF8C99", "#EF8C99", "#EF8C99", "#EF8C99", "#EF8C99", "#EF8C99", "#EF8C99"],
                borderWidth: .3,
                data: [35, 55, 65, 85, 40, 30, 50, 35, 50, 70, 60, 50]
            }]
        }
    }), new Chart(e, {
        type: "bar",
        options: {
            scales: {
                xAxes: [{
                    display: !0,
                    barPercentage: .2
                }],
                yAxes: [{
                    ticks: {
                        max: 100,
                        min: 0
                    },
                    display: !1
                }]
            },
            legend: {
                display: !1
            }
        },
        data: {
            labels: ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"],
            datasets: [{
                label: "Data Set 1",
                backgroundColor: ["#CF53F9", "#CF53F9", "#CF53F9", "#CF53F9", "#CF53F9", "#CF53F9", "#CF53F9", "#CF53F9", "#CF53F9", "#CF53F9", "#CF53F9", "#CF53F9"],
                borderColor: ["#CF53F9", "#CF53F9", "#CF53F9", "#CF53F9", "#CF53F9", "#CF53F9", "#CF53F9", "#CF53F9", "#CF53F9", "#CF53F9", "#CF53F9", "#CF53F9"],
                borderWidth: .2,
                data: [30, 40, 45, 55, 70, 45, 60, 35, 50, 63, 40, 70]
            }]
        }
    }), new Chart(a, {
        type: "line",
        options: {
            scales: {
                xAxes: [{
                    display: !0,
                    gridLines: {
                        display: !1
                    }
                }],
                yAxes: [{
                    ticks: {
                        max: 40,
                        min: 10,
                        stepSize: .1
                    },
                    display: !1,
                    gridLines: {
                        display: !1
                    }
                }]
            },
            legend: {
                display: !1
            }
        },
        data: {
            labels: ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "L", "M", "N", "O", "P", "Q", "R", "S", "T"],
            datasets: [{
                label: "Team Drills",
                fill: !0,
                lineTension: .3,
                backgroundColor: "transparent",
                borderColor: "#EF8C99",
                pointBorderColor: "#EF8C99",
                pointHoverBackgroundColor: "#EF8C99",
                borderCapStyle: "butt",
                borderDash: [],
                borderDashOffset: 0,
                borderJoinStyle: "miter",
                borderWidth: 2,
                pointBackgroundColor: "#EF8C99",
                pointBorderWidth: 2,
                pointHoverRadius: 4,
                pointHoverBorderColor: "#fff",
                pointHoverBorderWidth: 0,
                pointRadius: 1,
                pointHitRadius: 0,
                data: [20, 21, 25, 22, 24, 18, 20, 23, 19, 22, 25, 19, 24, 27, 22, 17, 20, 17, 20, 26, 22],
                spanGaps: !1
            }, {
                label: "Team Drills",
                fill: !0,
                lineTension: .3,
                backgroundColor: "transparent",
                borderColor: "rgba(238, 139, 152, 0.24)",
                pointBorderColor: "rgba(238, 139, 152, 0.24)",
                pointHoverBackgroundColor: "rgba(238, 139, 152, 0.24)",
                borderCapStyle: "butt",
                borderDash: [],
                borderDashOffset: 0,
                borderJoinStyle: "miter",
                borderWidth: 2,
                pointBackgroundColor: "rgba(238, 139, 152, 0.24)",
                pointBorderWidth: 2,
                pointHoverRadius: 4,
                pointHoverBorderColor: "#fff",
                pointHoverBorderWidth: 0,
                pointRadius: 1,
                pointHitRadius: 0,
                data: [24, 20, 23, 19, 22, 20, 25, 21, 23, 19, 21, 23, 19, 24, 19, 22, 21, 24, 19, 21, 20],
                spanGaps: !1
            }]
        }
    }), new Chart(t, {
        type: "line",
        options: {
            scales: {
                xAxes: [{
                    display: !0,
                    gridLines: {
                        display: !1
                    }
                }],
                yAxes: [{
                    ticks: {
                        max: 40,
                        min: 10,
                        stepSize: .1
                    },
                    display: !1,
                    gridLines: {
                        display: !1
                    }
                }]
            },
            legend: {
                display: !1
            }
        },
        data: {
            labels: ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "L", "M", "N", "O", "P", "Q", "R", "S", "T"],
            datasets: [{
                label: "Team Drills",
                fill: !0,
                lineTension: .3,
                backgroundColor: "transparent",
                borderColor: "#CF53F9",
                pointBorderColor: "#CF53F9",
                pointHoverBackgroundColor: "#CF53F9",
                borderCapStyle: "butt",
                borderDash: [],
                borderDashOffset: 0,
                borderJoinStyle: "miter",
                borderWidth: 2,
                pointBackgroundColor: "#CF53F9",
                pointBorderWidth: 2,
                pointHoverRadius: 4,
                pointHoverBorderColor: "#fff",
                pointHoverBorderWidth: 0,
                pointRadius: 1,
                pointHitRadius: 0,
                data: [24, 20, 23, 19, 22, 20, 25, 21, 23, 19, 21, 23, 19, 24, 19, 22, 21, 24, 19, 21, 20],
                spanGaps: !1
            }, {
                label: "Team Drills",
                fill: !0,
                lineTension: .3,
                backgroundColor: "transparent",
                borderColor: "rgba(207, 83, 249, 0.24)",
                pointBorderColor: "rgba(207, 83, 249, 0.24)",
                pointHoverBackgroundColor: "rgba(207, 83, 249, 0.24)",
                borderCapStyle: "butt",
                borderDash: [],
                borderDashOffset: 0,
                borderJoinStyle: "miter",
                borderWidth: 2,
                pointBackgroundColor: "rgba(207, 83, 249, 0.24)",
                pointBorderWidth: 2,
                pointHoverRadius: 4,
                pointHoverBorderColor: "#fff",
                pointHoverBorderWidth: 0,
                pointRadius: 1,
                pointHitRadius: 0,
                data: [20, 21, 25, 22, 24, 18, 20, 23, 19, 22, 25, 19, 24, 27, 22, 17, 20, 17, 20, 26, 22],
                spanGaps: !1
            }]
        }
    }), new Chart(d, {
        type: "bar",
        options: {
            scales: {
                xAxes: [{
                    display: !0,
                    gridLines: {
                        color: "transparent"
                    }
                }],
                yAxes: [{
                    display: !0,
                    gridLines: {
                        color: "transparent"
                    }
                }]
            }
        },
        data: {
            labels: ["January", "February", "March", "April", "May", "June", "July"],
            datasets: [{
                label: "Data Set 1",
                backgroundColor: ["#864DD9", "#864DD9", "#864DD9", "#864DD9", "#864DD9", "#864DD9", "#864DD9"],
                hoverBackgroundColor: ["#864DD9", "#864DD9", "#864DD9", "#864DD9", "#864DD9", "#864DD9", "#864DD9"],
                borderColor: ["#864DD9", "#864DD9", "#864DD9", "#864DD9", "#864DD9", "#864DD9", "#864DD9"],
                borderWidth: .5,
                data: [65, 59, 80, 81, 56, 55, 40]
            }, {
                label: "Data Set 2",
                backgroundColor: ["rgba(98, 98, 98, 0.5)", "rgba(98, 98, 98, 0.5)", "rgba(98, 98, 98, 0.5)", "rgba(98, 98, 98, 0.5)", "rgba(98, 98, 98, 0.5)", "rgba(98, 98, 98, 0.5)", "rgba(98, 98, 98, 0.5)"],
                hoverBackgroundColor: ["rgba(98, 98, 98, 0.5)", "rgba(98, 98, 98, 0.5)", "rgba(98, 98, 98, 0.5)", "rgba(98, 98, 98, 0.5)", "rgba(98, 98, 98, 0.5)", "rgba(98, 98, 98, 0.5)", "rgba(98, 98, 98, 0.5)"],
                borderColor: ["rgba(98, 98, 98, 0.5)", "rgba(98, 98, 98, 0.5)", "rgba(98, 98, 98, 0.5)", "rgba(98, 98, 98, 0.5)", "rgba(98, 98, 98, 0.5)", "rgba(98, 98, 98, 0.5)", "rgba(98, 98, 98, 0.5)"],
                borderWidth: .5,
                data: [35, 40, 60, 47, 88, 27, 30]
            }]
        }
    }), new Chart(n, {
        type: "pie",
        options: {
            legend: {
                display: !0,
                position: "left"
            }
        },
        data: {
            labels: ["A", "B", "C", "D"],
            datasets: [{
                data: [300, 50, 100, 80],
                borderWidth: 0,
                backgroundColor: ["#723ac3", "#864DD9", "#9762e6", "#a678eb"],
                hoverBackgroundColor: ["#723ac3", "#864DD9", "#9762e6", "#a678eb"]
            }]
        }
    }), new Chart(i, {
        type: "doughnut",
        options: {
            cutoutPercentage: 80,
            legend: {
                display: !0,
                position: "left"
            }
        },
        data: {
            labels: ["A", "B", "C", "D"],
            datasets: [{
                data: [120, 90, 77, 95],
                borderWidth: [0, 0, 0, 0],
                backgroundColor: ["#b53dde", "#CF53F9", "#d06cf2", "#de97f6"],
                hoverBackgroundColor: ["#b53dde", "#CF53F9", "#d06cf2", "#de97f6"]
            }]
        }
    });
    var C = {
        scale: {
            gridLines: {
                color: "#3f4145"
            },
            ticks: {
                beginAtZero: !0,
                min: 0,
                max: 100,
                stepSize: 20
            },
            pointLabels: {
                fontSize: 12
            }
        },
        legend: {
            position: "left"
        },
        elements: {
            arc: {
                borderWidth: 0,
                borderColor: "transparent"
            }
        }
    };
    new Chart(l, {
        type: "polarArea",
        options: C,
        data: {
            datasets: [{
                data: [80, 70, 60, 50],
                backgroundColor: ["#ba3fe4", "#CF53F9", "#d97bf9", "#e28eff"],
                label: "My dataset"
            }],
            labels: ["A", "B", "C", "D"]
        }
    }), C = {
        scale: {
            gridLines: {
                color: "#3f4145"
            },
            ticks: {
                beginAtZero: !0,
                min: 0,
                max: 100,
                stepSize: 20
            },
            pointLabels: {
                fontSize: 12
            }
        },
        legend: {
            position: "left"
        }
    }, new Chart(s, {
        type: "radar",
        options: C,
        data: {
            labels: ["A", "B", "C", "D", "E", "C"],
            datasets: [{
                label: "First dataset",
                backgroundColor: "rgba(113, 39, 172, 0.4)",
                borderWidth: 2,
                borderColor: "#7127AC",
                pointBackgroundColor: "#7127AC",
                pointBorderColor: "#fff",
                pointHoverBackgroundColor: "#fff",
                pointHoverBorderColor: "#7127AC",
                data: [65, 59, 90, 81, 56, 55]
            }, {
                label: "Second dataset",
                backgroundColor: "rgba(207, 83, 249, 0.4)",
                borderWidth: 2,
                borderColor: "#CF53F9",
                pointBackgroundColor: "#CF53F9",
                pointBorderColor: "#fff",
                pointHoverBackgroundColor: "#fff",
                pointHoverBorderColor: "#CF53F9",
                data: [50, 60, 80, 45, 96, 70]
            }]
        }
    })
}));
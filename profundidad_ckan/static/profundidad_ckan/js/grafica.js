$(function () {
    // Create the chart
    $('#grafica').highcharts({
        chart: {
            type: 'column'
        },
        title: {
            text: 'Tiempos de respuesta promedio para los diferentes Endpoints'
        },
        subtitle: {
            text: 'Para un límite de 100 datasets por consulta'
        },
        xAxis: {
            type: 'category'
        },
        yAxis: {
            title: {
                text: 'Tiempo'
            }

        },
        legend: {
            enabled: false
        },
        plotOptions: {
            series: {
                borderWidth: 0,
                dataLabels: {
                    enabled: true,
                    format: '{point.y:.1f}'
                }
            }
        },

        tooltip: {
            pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.2f}</b> Segundos<br/>'
        },

        series: [{
            name: 'Brands',
            colorByPoint: true,
            data: [{
                name: 'DBpedia',
                y: 0.372,
            }, {
                name: 'Europeana',
                y: 1.156,
            }, {
                name: 'Skos',
                y: 1.09,
            }, {
                name: 'datos_cl',
                y: 0.93,
            }, {
                name: 'British Library',
                y: 0.92,
            }]
        }],
    });
});
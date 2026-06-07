//consume http://127.0.0.1:8000/graficos

async function cargarGraficos() {

    const respuesta =
        await fetch("http://127.0.0.1:8000/graficos");

    const datos = await respuesta.json();

    const contenedor =
        document.getElementById("graficos");

    datos.forEach((grafico, index) => {

        const card =
            document.createElement("div");

        card.className = "grafico-card";

        const titulo =
            document.createElement("h2");

        titulo.textContent =
            grafico.pregunta;

        const canvas =
            document.createElement("canvas");

        canvas.id =
            "chart-" + index;

        card.appendChild(titulo);
        card.appendChild(canvas);

        contenedor.appendChild(card);

// Crear el gráfico con Chart.js
        new Chart(canvas, {

            type: "pie",

            data: {
                labels: grafico.labels,

                datasets: [{
                    data: grafico.values
                }]
            },

            plugins: [ChartDataLabels],

            options: {

                responsive: false,

                plugins: {

                    legend: {
                        position: "bottom"
                    },

                    datalabels: {

                        

                        formatter: (value) => {
                            return value;
                        },

                        font: {
                            weight: "bold",
                            size: 16
                        }
                    }
                }
            }
        });
    });
}

cargarGraficos();
// ==========================================
// CONSUME http://127.0.0.1:8000/graficos
// ==========================================


// ==========================================
// GRAFICO DE TORTA
// ==========================================

function crearGraficoTorta(canvas, grafico) {

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

                    formatter: (value) => value,

                    font: {
                        weight: "bold",
                        size: 16
                    }
                }
            }
        }
    });
}


// ==========================================
// GRAFICO DE BARRAS
// ==========================================

function crearGraficoBarras(canvas, grafico) {

    new Chart(canvas, {

        type: "bar",

        data: {
            labels: grafico.labels,

            datasets: [{
                label: grafico.pregunta,
                data: grafico.values
            }]
        },

        options: {

            responsive: false,

            scales: {

                y: {
                    beginAtZero: true
                }
            },

            plugins: {

                legend: {
                    display: false
                }
            }
        }
    });
}


// ==========================================
// CARGA TODOS LOS GRAFICOS
// ==========================================

async function cargarGraficos() {

    const respuesta =
        await fetch("http://127.0.0.1:8000/graficos");

    const datos =
        await respuesta.json();

    const contenedor =
        document.getElementById("graficos");

    datos.forEach((grafico, index) => {

        // ------------------------------
        // Crear tarjeta
        // ------------------------------

        const card =
            document.createElement("div");

        card.className = "grafico-card";

        // Clase según tipo de gráfico

        if (grafico.tipo_grafico === "bar") {

            card.classList.add("card-barras");

        } else {

            card.classList.add("card-torta");
        }

        // ------------------------------
        // Crear título
        // ------------------------------

        const titulo =
            document.createElement("h2");

        titulo.textContent =
            grafico.pregunta;

        // ------------------------------
        // Crear canvas
        // ------------------------------

        const canvas =
            document.createElement("canvas");

        canvas.id =
            "chart-" + index;

        // Clase según tipo de gráfico

        if (grafico.tipo_grafico === "bar") {

            canvas.classList.add("grafico-barras");

        } else {

            canvas.classList.add("grafico-torta");
        }

        // ------------------------------
        // Agregar elementos a la tarjeta
        // ------------------------------

        card.appendChild(titulo);
        card.appendChild(canvas);

        contenedor.appendChild(card);

        // ------------------------------
        // Crear gráfico correspondiente
        // ------------------------------

        if (grafico.tipo_grafico === "bar") {

            crearGraficoBarras(canvas, grafico);

        } else {

            crearGraficoTorta(canvas, grafico);
        }
    });
}


// ==========================================
// INICIO
// ==========================================

cargarGraficos();
//para mostrar el resumen de las encuestas en el dashboard

async function cargarResumen() {

    const respuesta =
        await fetch("http://127.0.0.1:8000/resumen");

    const resumen =
        await respuesta.json();

    document.getElementById("resumen").innerHTML = `
        <p>Total de respuestas: ${resumen.total_respuestas}</p>
        <p>Total de preguntas: ${resumen.total_preguntas}</p>
    `;
}

cargarResumen();
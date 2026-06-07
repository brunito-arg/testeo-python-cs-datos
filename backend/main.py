from fastapi import FastAPI

from backend.services.analisis_encuestas import (
    obtener_preguntas,
    obtener_estadisticas,
    obtener_graficos
)

app = FastAPI()

@app.get("/")
def home():
    return {
        "mensaje": "Backend funcionando"
    }

@app.get("/preguntas")
def preguntas():
    return obtener_preguntas()

@app.get("/estadisticas/{pregunta}")
def estadisticas(pregunta: str):
    return obtener_estadisticas(pregunta)

@app.get("/graficos")
def graficos():

    return obtener_graficos()
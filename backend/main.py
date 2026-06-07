from fastapi import FastAPI

from backend.services.analisis_encuestas import (
    obtener_preguntas,
    obtener_estadisticas,
    obtener_graficos
)

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
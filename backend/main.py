from fastapi import FastAPI

from backend.services.analisis_encuestas import obtener_preguntas

app = FastAPI()

@app.get("/")
def home():

    return {
        "mensaje": "Backend funcionando"
    }

@app.get("/preguntas")
def preguntas():

    return obtener_preguntas()
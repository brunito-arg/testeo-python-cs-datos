import pandas as pd

URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQuM2Y9QqcH_1LIkmdHHflDYTK7y3u9jgUlmZ-XYzaky7HYNyN3_DceBNSagYXESgdYZgnKSRIv5CkU/pub?gid=1237250350&single=true&output=csv"

def get_data():
    return pd.read_csv(URL)

def obtener_preguntas():
    df = get_data()
    return list(df.columns)

def obtener_estadisticas(pregunta):

    df = get_data()

    if pregunta not in df.columns:
        return {"error": "Pregunta no encontrada"}

    conteo = df[pregunta].value_counts()

    return {
        "pregunta": pregunta,
        "labels": conteo.index.tolist(),
        "values": conteo.values.tolist()
    }


def obtener_graficos():

    df = get_data()

    resultado = []

    for columna in df.columns:

        # Opcional: ignorar marca temporal
        if columna.lower() == "marca temporal":
            continue

        conteo = df[columna].value_counts()

        resultado.append({
            "pregunta": columna,
            "labels": conteo.index.tolist(),
            "values": conteo.values.tolist()
        })

    return resultado

def obtener_resumen():

    df = get_data()

    total_preguntas = len(df.columns)

    if "Marca temporal" in df.columns:
        total_preguntas -= 1

    return {
        "total_respuestas": len(df),
        "total_preguntas": total_preguntas
    }
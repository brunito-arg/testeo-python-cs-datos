import pandas as pd

URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQuM2Y9QqcH_1LIkmdHHflDYTK7y3u9jgUlmZ-XYzaky7HYNyN3_DceBNSagYXESgdYZgnKSRIv5CkU/pub?gid=1237250350&single=true&output=csv"


def get_data():
    return pd.read_csv(URL)


def obtener_preguntas():
    df = get_data()
    return list(df.columns)

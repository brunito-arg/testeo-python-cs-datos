import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

st.title("Encuesta - Visualizador de gráficos")

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQuM2Y9QqcH_1LIkmdHHflDYTK7y3u9jgUlmZ-XYzaky7HYNyN3_DceBNSagYXESgdYZgnKSRIv5CkU/pub?gid=1237250350&single=true&output=csv"

@st.cache_data
def load_data(u):
    return pd.read_csv(u)


df = load_data(url)

st.write("Fuente:", url)
st.dataframe(df.head())

# Columnas candidatas a mostrar (categóricas / pocas categorías)
cat_cols = [c for c in df.columns if df[c].dtype == 'object' or df[c].nunique() <= 20]
if not cat_cols:
    st.error("No se encontraron columnas categóricas para graficar.")
else:
    default = "estas feliz" if "estas feliz" in cat_cols else cat_cols[0]
    sel = st.selectbox("Selecciona la columna a graficar", cat_cols, index=cat_cols.index(default))

    vc = df[sel].value_counts().sort_index()

    fig, ax = plt.subplots()
    vc.plot(kind='bar', ax=ax)
    ax.set_title(sel)
    ax.set_xlabel("Respuesta")
    ax.set_ylabel("Cantidad de personas")
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    plt.tight_layout()

    st.pyplot(fig)

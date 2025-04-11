import streamlit as st
import pandas as pd

st.set_page_config(page_title="Controle de Abastecimento", layout="wide")

st.title("📊 Controle de Abastecimento")

@st.cache_data
def carregar_dados():
    return pd.read_excel("consumo.xlsx")

try:
    df = carregar_dados()
    st.success("Dados carregados com sucesso!")
    
    st.dataframe(df, use_container_width=True)

    if st.checkbox("Mostrar estatísticas"):
        st.write("Resumo estatístico:")
        st.write(df.describe())

    if st.checkbox("Mostrar gráfico de consumo"):
        if "média de consumo" in df.columns:
            st.line_chart(df["média de consumo"])
        else:
            st.warning("Coluna 'média de consumo' não encontrada no arquivo.")

except Exception as e:
    st.error(f"Erro ao carregar o arquivo: {e}")

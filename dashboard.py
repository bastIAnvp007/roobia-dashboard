
import streamlit as st
import pandas as pd

# ------------------ Cargar datos reales ------------------

try:
    df = pd.read_csv("resultados_2025.csv")
except FileNotFoundError:
    st.warning("⚠️ No se encontró el archivo 'resultados_2025.csv'. Sube uno nuevo al repositorio.")
    st.stop()

# ------------------ UI Streamlit ------------------

st.set_page_config(page_title="RooBIA Dashboard", layout="centered")

st.title("📊 RooBIA - Dashboard Inmobiliario")
st.markdown("Visualización de resultados obtenidos desde Telegram Bot")

# Filtros
comunas = df['comuna'].unique()
comuna = st.selectbox("📍 Filtrar por comuna", options=["Todas"] + list(comunas))

presupuesto = st.slider("💰 Filtrar por presupuesto máximo (CLP)", min_value=500000, max_value=3000000, value=1000000, step=50000)

# Aplicar filtros
df_filtrado = df.copy()

if comuna != "Todas":
    df_filtrado = df_filtrado[df_filtrado['comuna'] == comuna]

df_filtrado = df_filtrado[df_filtrado['precio_clp'] <= presupuesto]

# Mostrar resultados
st.subheader(f"🔎 {len(df_filtrado)} resultados encontrados")

if df_filtrado.empty:
    st.info("😕 No se encontraron propiedades que cumplan los criterios.")
else:
    for _, row in df_filtrado.iterrows():
        st.markdown(f"### {row['titulo']}")
        st.markdown(f"- 💰 {row['precio']}")
        st.markdown(f"- 📍 {row['comuna']}")
        st.markdown(f"- 🔗 [Ver propiedad]({row['link']})")
        st.markdown("---")


import streamlit as st
import pandas as pd

# Simular datos desde RooBIA
data = [
    {"titulo": "Depto Ronda Santo Domingo", "precio": "22 UF (≈ $803.000 CLP)", "precio_clp": 803000, "comuna": "Santiago", "link": "https://portalinmobiliario.com/MLC-123"},
    {"titulo": "Casa Ñuñoa Vista Oriente", "precio": "$720.000 CLP", "precio_clp": 720000, "comuna": "Ñuñoa", "link": "https://portalinmobiliario.com/MLC-456"},
    {"titulo": "Depto Providencia Metro", "precio": "24 UF (≈ $876.000 CLP)", "precio_clp": 876000, "comuna": "Providencia", "link": "https://portalinmobiliario.com/MLC-789"},
]

df = pd.DataFrame(data)

# ------------------ UI Streamlit ------------------

st.set_page_config(page_title="RooBIA Dashboard", layout="centered")

st.title("📊 RooBIA - Dashboard Inmobiliario")
st.markdown("Visualización de resultados obtenidos desde Telegram Bot")

# Filtros
comunas = df['comuna'].unique()
comuna = st.selectbox("📍 Filtrar por comuna", options=["Todas"] + list(comunas))

presupuesto = st.slider("💰 Filtrar por presupuesto máximo (CLP)", min_value=500000, max_value=1500000, value=1000000, step=50000)

# Aplicar filtros
df_filtrado = df.copy()

if comuna != "Todas":
    df_filtrado = df_filtrado[df_filtrado['comuna'] == comuna]

df_filtrado = df_filtrado[df_filtrado['precio_clp'] <= presupuesto]

# Mostrar resultados
st.subheader(f"🔎 {len(df_filtrado)} resultados encontrados")

for _, row in df_filtrado.iterrows():
    st.markdown(f"### {row['titulo']}")
    st.markdown(f"- 💰 {row['precio']}")
    st.markdown(f"- 🔗 [Ver propiedad]({row['link']})")
    st.markdown("---")

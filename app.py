import streamlit as st
import pandas as pd
import plotly.express as px

# --- CONFIGURACIÓN DE LA PÁGINA (Mejora la UX/UI) ---
st.set_page_config(
    page_title="LVBP Stars Dashboard",
    page_icon="⚾",
    layout= "wide"
)

# El código limpia y transforma los datos para análisis.
def cargar_y_procesar():
    df = pd.read_csv('jugadores_lvbp.csv') 
    df['AVG'] = (df['H'] / df['VB']).round(3)
    df.index = range(1, len(df) + 1)
    return df

df = cargar_y_procesar()

st.title("⚾ LVBP Analisis: Temporada 2025-2026")
st.markdown("---")


col1, col2, col3 = st.columns(3)

# Calculamos líderes usando pandas
lider_hr = df.loc[df['HR'].idxmax()]
lider_avg = df.loc[df['AVG'].idxmax()]

with col1:
    st.metric(label="🔥 Líder de Jonrones", value=lider_hr['Nombre'], delta=f"{lider_hr['HR']} HR")
with col2:
    st.metric(label="🎯 Mejor Promedio", value=lider_avg['Nombre'], delta=f"{lider_avg['AVG']} AVG")
with col3:
    st.metric(label="🏟️ Total Jugadores", value=len(df))

st.markdown("---")

# Barra lateral para navegación
st.sidebar.header("Panel de Filtros")
equipo = st.sidebar.selectbox("Selecciona un Equipo:", ['Todos'] + list(df['Equipo'].unique()))

if equipo != 'Todos':
    df_final = df[df['Equipo'] == equipo]
else:
    df_final = df

st.subheader(f"📊 Análisis de Jugadores: {equipo}")
# Usamos plotly
fig = px.bar(
    df_final, 
    x='HR', 
    y='Nombre', 
    orientation='h',
    color='AVG', # El color cambia según el promedio
    title=f"Jonrones y Rendimiento: {equipo}",
    labels={'HR': 'Jonrones', 'AVG': 'Promedio de Bateo'},
    template="plotly_dark"
)
fig.update_layout(yaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig, use_container_width=True)

# Tabla de datos detallada
st.subheader("📋 Detalle de Jugadores")
st.dataframe(df_final, use_container_width=True)


st.markdown("---")

st.write("**Proyecto realizado por:**")
st.write("- Juan Jaure")
st.write("- Darwin Mendoza")
st.write("- Rayan Herrera")
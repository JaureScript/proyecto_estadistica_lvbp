import streamlit as st
import pandas as pd
import plotly.express as px

# configuracion principal de la pagina
st.set_page_config(
    page_title="LVBP Stars Dashboard",
    page_icon="⚾",
    layout= "wide"
)

#para procesar los datos
def cargar_y_procesar():
    df = pd.read_csv('jugadores_lvbp.csv') 
    df['AVG'] = (df['H'] / df['VB']).round(3)
    df['Poder'] = (df['HR'] * 10) + (df['AVG'] * 1000)
    df.index = range(1, len(df) + 1)
    return df

df = cargar_y_procesar()

#barrra lateral
st.sidebar.header("🔍 Panel de Control")
equipo = st.sidebar.selectbox("Selecciona un Equipo:", ['Todos'] + list(df['Equipo'].unique()))
nombre_buscar = st.sidebar.text_input("Buscar Jugador por nombre:")

df_final = df.copy()
if equipo != 'Todos':
    df_final = df_final[df_final['Equipo'] == equipo]
if nombre_buscar:
    df_final = df_final[df_final['Nombre'].str.contains(nombre_buscar, case=False)]

df_final.index = range(1, len(df_final) + 1)

#titulo principal
st.title("⚾ LVBP Analisis: Temporada 2025-2026")
st.markdown("---")

#pandas para metricas
col1, col2, col3 = st.columns(3)
lider_hr = df.loc[df['HR'].idxmax()]
lider_avg = df.loc[df['AVG'].idxmax()]

with col1:
    st.metric(label="🔥 Líder de Jonrones", value=lider_hr['Nombre'], delta=f"{lider_hr['HR']} HR")
with col2:
    st.metric(label="🎯 Mejor Promedio", value=lider_avg['Nombre'], delta=f"{lider_avg['AVG']} AVG")
with col3:
    st.metric(label="🏟️ Total Jugadores", value=len(df))

st.markdown("---")

st.subheader(f"📊 Gráfico de Rendimiento: {equipo}")

# 1. Definimos los colores oficiales de TODOS los equipos
colores_equipos = {
    'Leones': "#FBAB33",       # Amarillo
    'Magallanes': '#0047AB', # Azul Eléctrico
    'Tiburones': '#E74C3C',    # Rojo/Samba
    'Cardenales': '#C0392B',        # Rojo Cardenal
    'Tigres': '#000080',          # Azul Marino (o Naranja #F39C12 si prefieres)
    'Aguilas': '#FF8C00',         # Naranja
    'Bravos': '#00FFFF',       # Cian/Turquesa
    'Caribes': '#FFD700'      # Dorado/Naranja
}

# 2. Configuración inteligente del gráfico
fig = px.bar(
    df_final, 
    x='HR', 
    y='Nombre', 
    orientation='h',
    
    # AQUÍ ESTÁ LA CLAVE:
    color='Equipo',  # <-- Le dice a Plotly: "Pinta según el equipo del jugador"
    color_discrete_map=colores_equipos, # <-- "Usa este diccionario para saber qué color toca"
    
    title=f"Jonrones por Jugador: {equipo}",
    labels={'HR': 'Jonrones', 'AVG': 'Promedio', 'Equipo': 'Club'},
    template="plotly_dark"
)

fig.update_layout(yaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig, use_container_width=True)

# Tabla de datos detallada
st.subheader("📋 Detalle de Jugadores")
st.dataframe(df_final, use_container_width=True)


st.markdown("---")

st.write("**Equipo de trabajo**")
st.write("- Juan Jaure")
st.write("- Darwin Mendoza")
st.write("- Rayan Herrera")
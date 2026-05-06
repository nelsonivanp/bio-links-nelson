import streamlit as st
import base64
import os
import pandas as pd
from datetime import datetime

# 1. Configuración de la app
st.set_page_config(page_title="Nelson Peña | Contactos", page_icon="🔗", layout="centered")

# --- SISTEMA DE MÉTRICAS ---
archivo_metricas = "metricas_bio.csv"
if not os.path.exists(archivo_metricas):
    pd.DataFrame(columns=["Fecha", "Tipo_Evento", "Detalle"]).to_csv(archivo_metricas, index=False)

if 'visita_registrada' not in st.session_state:
    df = pd.read_csv(archivo_metricas)
    nueva_visita = {"Fecha": datetime.now().strftime("%d/%m/%Y %H:%M:%S"), "Tipo_Evento": "Visita a Página", "Detalle": "Inicio"}
    df = pd.concat([df, pd.DataFrame([nueva_visita])], ignore_index=True)
    df.to_csv(archivo_metricas, index=False)
    st.session_state['visita_registrada'] = True

# --- FUNCIÓN PARA CARGAR FONDO ---
def get_base64_of_bin_file(bin_file):
    try:
        with open(bin_file, 'rb') as f: return base64.b64encode(f.read()).decode()
    except FileNotFoundError: return ""

img_base64_fondo = get_base64_of_bin_file("fondo.png")

# --- ESTILOS CSS (ARIAL Y FIX DE ALINEACIÓN) ---
st.markdown(f"""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
<style>
    /* Fondo e Interfaz */
    [data-testid="stAppViewContainer"] {{
        background-image: url('data:image/png;base64,{img_base64_fondo}') !important;
        background-size: cover !important;
        background-position: center !important;
        background-attachment: fixed !important;
    }}
    [data-testid="stHeader"] {{ background: transparent !important; }}
    header {{visibility: hidden;}}

    /* Cabecero con Tipografía Arial */
    .header-container {{
        text-align: center;
        margin-bottom: 40px;
        padding: 20px;
        border-bottom: 1px solid rgba(0, 168, 232, 0.5);
        font-family: Arial, sans-serif;
    }}
    .header-nombre {{
        font-weight: bold;
        font-size: 30px;
        color: white;
        letter-spacing: 1px;
    }}
    .header-bio {{
        font-style: italic;
        font-size: 16px;
        color: #00A8E8;
        margin-top: 5px;
    }}
    .header-user {{
        font-style: italic;
        font-size: 14px;
        color: #cccccc;
    }}

    /* Botones Centrados con Ícono Fijo a la Izquierda */
    .boton-link {{
        position: relative; /* Esto nos permite fijar el ícono */
        display: flex;
        align-items: center;
        justify-content: center; /* Centra el texto perfectamente */
        width: 100%;
        padding: 18px 20px;
        margin: 15px 0;
        background: rgba(255, 255, 255, 0.07); 
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 12px;
        color: white !important;
        text-decoration: none;
        transition: 0.3s;
        font-family: Arial, sans-serif;
    }}
    
    .icon-box {{
        position: absolute; /* Saca el ícono del centro y lo pega a la izquierda */
        left: 25px;
        font-size: 24px;
        color: white;
    }}
    
    .link-text {{
        font-size: 17px;
        font-weight: 400;
        text-align: center;
        width: 100%;
    }}

    .boton-link:hover {{
        background: rgba(255, 255, 255, 0.15);
        border-color: #00A8E8;
        transform: translateY(-2px);
    }}
</style>
""", unsafe_allow_html=True)

# --- CABECERO ---
st.markdown('''
<div class="header-container">
    <div class="header-nombre">NELSON IVAN PEÑA</div>
    <div class="header-bio">PUBLICISTA Y ESTRATEGA DIGITAL</div>
    <div class="header-user">@nelsonivanp</div>
</div>
''', unsafe_allow_html=True)

# --- BOTONES DE ENLACE ---
redes = [
    {"icon": "fab fa-instagram", "text": "Únete a la comunidad", "url": "https://instagram.com/nelsonivanp"},
    {"icon": "fab fa-instagram", "text": "Portafolio Fotográfico", "url": "https://instagram.com/nelsonivanphotos"},
    {"icon": "fab fa-tiktok", "text": "Mis videos como hobbie", "url": "https://tiktok.com/@nelsonivanp"},
    {"icon": "fab fa-linkedin-in", "text": "Trayectoria Profesional", "url": "https://linkedin.com/in/nelsonivanp"},
    {"icon": "fa-brands fa-threads", "text": "Conversemos de temas varios", "url": "https://threads.net/@nelsonivanp"},
    {"icon": "fab fa-youtube", "text": "Próximamente mi Canal de Youtube", "url": "https://youtube.com/@nelsonivanp"},
    {"icon": "fab fa-whatsapp", "text": "Contáctame", "url": "https://wa.me/584226357667"}
]

for red in redes:
    st.markdown(f'''
    <a href="{red["url"]}" target="_blank" class="boton-link">
        <div class="icon-box"><i class="{red["icon"]}"></i></div>
        <div class="link-text">{red["text"]}</div>
    </a>
    ''', unsafe_allow_html=True)

# --- SECCIÓN ADMINISTRADOR (100% INVISIBLE) ---
# Solo se muestra si entras con un "pase especial" en la dirección web
if "modo" in st.query_params and st.query_params["modo"] == "admin":
    st.write("---")
    st.markdown("<h3 style='text-align: center; color: #00A8E8; font-family: Arial;'>🕵️‍♂️ Panel de Control Oculto</h3>", unsafe_allow_html=True)
    try:
        df_m = pd.read_csv(archivo_metricas)
        st.dataframe(df_m)
        st.metric(label="Visitas Totales a la Bio", value=len(df_m))
    except:
        st.write("Aún no hay datos.")

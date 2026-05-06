import streamlit as st
import base64
import os
import pandas as pd
from datetime import datetime

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="Nelson Peña | Bio", page_icon="🔗", layout="centered")

# --- MÉTRICAS ---
archivo_metricas = "metricas_bio.csv"
if not os.path.exists(archivo_metricas):
    pd.DataFrame(columns=["Fecha", "Tipo_Evento", "Detalle"]).to_csv(archivo_metricas, index=False)

# --- FUNCIÓN PARA CARGAR IMÁGENES LOCALES ---
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Cargamos el header del Ávila
header_base64 = get_base64("header1.png")

# --- ESTILOS CSS (DISEÑO PREMIUM CON HEADER DE IMAGEN) ---
st.markdown(f"""
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
<style>
    /* Fondo Negro Puro */
    [data-testid="stAppViewContainer"] {{
        background-color: #080808 !important;
    }}
    [data-testid="stHeader"] {{ background: transparent !important; }}
    header {{visibility: hidden;}}

    /* Contenedor del Header de Imagen */
    .header-img-container {{
        width: 100%;
        margin-top: -60px; /* Pegado al techo */
        margin-bottom: 30px;
        text-align: center;
    }}
    .header-img-container img {{
        width: 100%;
        max-width: 800px;
        border-radius: 0 0 20px 20px;
        box-shadow: 0px 10px 30px rgba(0, 168, 232, 0.2);
        border-bottom: 2px solid #D4AF37; /* Línea dorada de remate */
    }}

    /* Botones Estilo Cristal con Borde Azul */
    .boton-link {{
        display: flex;
        align-items: center;
        width: 100%;
        padding: 18px 25px;
        margin: 15px 0;
        background: rgba(255, 255, 255, 0.03); 
        border: 1px solid rgba(0, 168, 232, 0.5); 
        border-radius: 12px;
        color: white !important;
        text-decoration: none !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        font-family: 'Montserrat', sans-serif;
    }}
    
    .icon-box {{
        font-size: 22px;
        color: #00A8E8;
        min-width: 45px;
    }}
    
    .link-text {{
        font-size: 16px;
        font-weight: 400;
        text-align: center;
        flex-grow: 1;
        padding-right: 45px;
    }}

    /* Efecto Dorado al pasar el cursor */
    .boton-link:hover {{
        background: linear-gradient(90deg, rgba(212, 175, 55, 0.1) 0%, rgba(212, 175, 55, 0.2) 100%);
        border-color: #D4AF37;
        box-shadow: 0px 0px 20px rgba(212, 175, 55, 0.4);
        transform: scale(1.02);
        color: #D4AF37 !important;
    }}

    .boton-link:hover .icon-box {{
        color: #D4AF37;
    }}
</style>
""", unsafe_allow_html=True)

# --- MOSTRAR EL HEADER (LA FOTO DEL ÁVILA) ---
st.markdown(f'''
<div class="header-img-container">
    <img src="data:image/png;base64,{header_base64}" alt="Nelson Peña Header">
</div>
''', unsafe_allow_html=True)

# --- BOTONES (Contenido actualizado) ---
redes = [
    {"icon": "fab fa-instagram", "text": "Únete a la comunidad", "url": "https://instagram.com/nelsonivanp"},
    {"icon": "fas fa-camera-retro", "text": "Portafolio Fotográfico", "url": "https://instagram.com/nelsonivanphotos"},
    {"icon": "fab fa-tiktok", "text": "Mis videos como hobbie", "url": "https://tiktok.com/@nelsonivanp"},
    {"icon": "fab fa-linkedin-in", "text": "Trayectoria Profesional", "url": "https://linkedin.com/in/nelsonivanp"},
    {"icon": "fa-brands fa-threads", "text": "Conversemos de temas varios", "url": "https://threads.net/@nelsonivanp"},
    {"icon": "fab fa-youtube", "text": "Próximamente mi Canal de Youtube", "url": "https://youtube.com/@nelsonivanp"},
    {"icon": "fab fa-whatsapp", "text": "Contáctame", "url": "https://wa.me/"} # Número omitido por privacidad
]

for red in redes:
    st.markdown(f'''
    <a href="{red["url"]}" target="_blank" class="boton-link">
        <div class="icon-box"><i class="{red["icon"]}"></i></div>
        <div class="link-text">{red["text"]}</div>
    </a>
    ''', unsafe_allow_html=True)

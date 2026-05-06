import streamlit as st
import base64
import os
import pandas as pd
from datetime import datetime

# 1. Configuración de la app (Título en pestaña de navegador)
st.set_page_config(page_title="Nelson Peña | Contactos", page_icon="🔗", layout="centered")

# --- SISTEMA DE MÉTRICAS (Mantenemos la lógica existente) ---
archivo_metricas = "metricas_bio.csv"
if not os.path.exists(archivo_metricas):
    pd.DataFrame(columns=["Fecha", "Tipo_Evento", "Detalle"]).to_csv(archivo_metricas, index=False)

if 'visita_registrada' not in st.session_state:
    df = pd.read_csv(archivo_metricas)
    nueva_visita = {"Fecha": datetime.now().strftime("%d/%m/%Y %H:%M:%S"), "Tipo_Evento": "Visita a Página", "Detalle": "Inicio"}
    df = pd.concat([df, pd.DataFrame([nueva_visita])], ignore_index=True)
    df.to_csv(archivo_metricas, index=False)
    st.session_state['visita_registrada'] = True

# --- FUNCIÓN PARA CARGAR FONDO "NP" ---
def get_base64_of_bin_file(bin_file):
    try:
        with open(bin_file, 'rb') as f: return base64.b64encode(f.read()).decode()
    except FileNotFoundError: return ""

img_base64_fondo = get_base64_of_bin_file("fondo.png")

# --- ESTILOS CSS AVANZADOS (Tech Authority + Creative Edge + Luxury Minimalist) ---
st.markdown(f"""
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;500;700&family=Orbitron:wght@500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
<style>
    /* Fondo e Interfaz Base (Usando tu imagen np) */
    [data-testid="stAppViewContainer"] {{
        background-image: url('data:image/png;base64,{img_base64_fondo}') !important;
        background-size: cover !important;
        background-position: center !important;
        background-attachment: fixed !important;
    }}
    [data-testid="stHeader"] {{ background: transparent !important; }}
    header {{visibility: hidden;}}

    /* Cabecero Integrado (Navy Cyan Tinted Panel) */
    .header-container {{
        text-align: center;
        margin-bottom: 40px;
        padding: 30px;
        background: rgba(0, 30, 45, 0.4); /* Tinte navy sutil */
        border-radius: 15px;
        border-bottom: 2px solid #00A8E8; /* Borde inferior eléctrico */
        box-shadow: 0px 5px 15px rgba(0, 168, 232, 0.2);
    }}
    .header-nombre {{
        font-family: 'Orbitron', sans-serif; /* Futurista para el nombre */
        font-weight: bold;
        font-size: 32px;
        color: white;
        letter-spacing: 2px;
        text-transform: uppercase;
    }}
    .header-bio {{
        font-family: 'Montserrat', sans-serif;
        font-style: italic;
        font-size: 16px;
        color: #00A8E8; /* Azul cyan para contraste */
        margin-top: 8px;
    }}
    .header-user {{
        font-family: 'Montserrat', sans-serif;
        font-style: italic;
        font-size: 14px;
        color: #cccccc;
        margin-top: 2px;
    }}

    /* Botones de Cristal Ahumado (Glassmorphism con Borde Neón) */
    .boton-link {{
        position: relative;
        display: flex;
        align-items: center;
        justify-content: center; /* Centrado perfecto del texto */
        width: 100%;
        padding: 18px 25px;
        margin: 16px 0;
        background: rgba(255, 255, 255, 0.05); /* Cristal semi-transparente */
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(0, 168, 232, 0.3); /* Borde fino cyan */
        border-radius: 15px;
        color: white !important;
        text-decoration: none !important; /* Elimina subrayado */
        transition: 0.3s ease;
        font-family: 'Montserrat', sans-serif;
    }}
    
    /* Cajón del Ícono (Fijo a la izquierda) */
    .icon-box {{
        position: absolute;
        left: 20px;
        font-size: 24px;
        color: white;
    }}
    
    /* Texto del Link (Totalmente centrado) */
    .link-text {{
        font-size: 17px;
        font-weight: 500;
        text-align: center;
        width: 100%;
        text-shadow: 0px 1px 3px rgba(0, 0, 0, 0.5);
    }}

    /* Efecto Hover (Iluminación Neón) */
    .boton-link:hover {{
        background: rgba(255, 255, 255, 0.1);
        border-color: #00A8E8; /* Borde más brillante */
        box-shadow: 0px 0px 10px rgba(0, 168, 232, 0.5); /* Brillo neón externo */
        transform: translateY(-3px); /* Pequeño salto creativo */
    }}
</style>
""", unsafe_allow_html=True)

# --- CABECERO CON ESTILO INTEGRADO ---
st.markdown('''
<div class="header-container">
    <div class="header-nombre">NELSON IVAN PEÑA</div>
    <div class="header-bio">PUBLICISTA Y ESTRATEGA DIGITAL</div>
    <div class="header-user">@nelsonivanp</div>
</div>
''', unsafe_allow_html=True)

# --- BOTONES DE ENLACE (Mantenemos TEXTO EXACTO y actualizamos ÍCONOS) ---
redes = [
    {"icon": "fab fa-instagram", "text": "Únete a la comunidad", "url": "https://instagram.com/nelsonivanp"},
    {"icon": "fas fa-camera-retro", "text": "Portafolio Fotográfico", "url": "https://instagram.com/nelsonivanphotos"}, # Actualizado a Cámara
    {"icon": "fab fa-tiktok", "text": "Mis videos como hobbie", "url": "https://tiktok.com/@nelsonivanp"},
    {"icon": "fab fa-linkedin-in", "text": "Trayectoria Profesional", "url": "https://linkedin.com/in/nelsonivanp"},
    {"icon": "fa-brands fa-threads", "text": "Conversemos de temas varios", "url": "https://threads.net/@nelsonivanp"}, # Icono oficial Threads
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
# Mantenemos el acceso secreto vía ?modo=admin
if "modo" in st.query_params and st.query_params["modo"] == "admin":
    st.write("---")
    st.markdown("<h3 style='text-align: center; color: #00A8E8; font-family: 'Orbitron', sans-serif;'>🕵️‍♂️ Panel de Control Oculto</h3>", unsafe_allow_html=True)
    try:
        df_m = pd.read_csv(archivo_metricas)
        st.dataframe(df_m)
        st.metric(label="Visitas Totales a la Bio", value=len(df_m))
    except:
        st.write("Aún no hay datos.")

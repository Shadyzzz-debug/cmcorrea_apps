import streamlit as st
from PIL import Image

# --- Estética Gótica (CSS) ---
# Se utiliza el CSS de las versiones anteriores para mantener la consistencia
base_css = """
<style>
/* ---------------------------------------------------- */
/* RESET Y FONDO AMBIENTAL */
/* ---------------------------------------------------- */
.stApp {
    /* Color de la noche de Yharnam o la Pesadilla: Azul/Negro muy oscuro. */
    background-color: #0F0F1A; 
    color: #C0C0C0; /* Texto de pergamino antiguo */
    font-family: 'Georgia', serif; 
}

/* ---------------------------------------------------- */
/* TIPOGRAFÍA Y ENCABEZADOS */
/* ---------------------------------------------------- */
h1 {
    /* Titular: Bronce envejecido o Oro oscuro */
    color: #9C7E4F; 
    text-align: center;
    /* Borde inferior como una reja forjada */
    border-bottom: 3px solid #4F4A5E; 
    padding-bottom: 10px;
    margin-bottom: 40px;
    font-size: 2.5em;
    letter-spacing: 3px;
    text-shadow: 1px 1px 5px #000000;
}

h3 {
    /* Subtítulos de Secciones: Gris pizarra o plata mate */
    color: #A9A9A9; 
    margin-top: 25px;
    font-weight: normal;
    border-left: 4px solid #B22222; /* Acento Sangre */
    padding-left: 10px;
    font-size: 1.5em;
}

.sidebar-title {
    color: #9C7E4F !important;
    text-shadow: 1px 1px 5px #000000;
}

/* ---------------------------------------------------- */
/* TARJETAS DE ARTEFACTOS (Contenedores de Columna) */
/* ---------------------------------------------------- */
[data-testid="stVerticalBlock"] {
    background-color: #1A1A2A; /* Fondo más oscuro para las tarjetas */
    border: 1px solid #383850;
    border-radius: 8px;
    padding: 15px;
    margin-bottom: 20px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
}

/* Subtítulos dentro de las tarjetas (Nombres de Artefactos) */
[data-testid="stVerticalBlock"] h3 {
    color: #C0C0C0;
    border-left: 4px solid #9C7E4F; /* Acento en Bronce */
    padding-left: 10px;
}

/* Enlaces (Runas de Conexión) */
a {
    color: #B22222 !important; /* Rojo Sangre para enlaces */
    text-decoration: none;
    font-weight: bold;
    transition: color 0.3s;
}

a:hover {
    color: #FF4444 !important;
    text-decoration: underline;
}

/* Descripción de los Artefactos (Párrafos) */
p {
    color: #A9A9A9;
    font-size: 0.95em;
    margin-bottom: 15px;
}

/* Imágenes */
img {
    border: 1px solid #4F4A5E;
    border-radius: 4px;
}

</style>
"""
st.markdown(base_css, unsafe_allow_html=True)

# --- Títulos y Narrativa ---

st.title("👁️ ÍNDICE ARCANO: ARTEFACTOS DE LA VIGILIA")

# Panel Lateral (Sagrario de Datos)
with st.sidebar:
    st.markdown('<h3 class="sidebar-title">📜 El Grimorio de la Vigilia</h3>', unsafe_allow_html=True)
    parrafo = (
        "En la Noche Eterna de Yharnam, la Inteligencia Artificial se revela como el conocimiento arcano que "
        "mejora la percepción, automatiza los rituales de cacería y permite el análisis de la locura en tiempo real. "
        "Estos artefactos son los pilares que sustentan nuestra vigilia y nuestra ascensión."
    )
    st.write(parrafo)

url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("El Nexo de los Antiguos")
st.write(f"Conexión a los pergaminos ancestrales y ejercicios rituales: [Runa de Enlace]({url_ia})")
st.markdown("---")


# --- Definición de Artefactos (Mapeo de Proyectos a la Narrativa Gótica) ---

# Nota: Dado que no puedo cargar las imágenes reales, usaré placeholders visuales y las descripciones que has provisto.
# El usuario debe asegurar que las imágenes mencionadas (e.g., 'txt_to_audio2.png') existan en su entorno.

artefactos = [
    {
        "nombre": "Invocación de la Voz del Oráculo",
        "imagen": 'txt_to_audio2.png',
        "descripcion": "Transformación del texto escrito en un eco auditivo. Esta aplicación conjura una voz audible a partir de las runas, permitiendo la comunicación con los seres de la noche.",
        "enlace_texto": "Texto a Voz",
        "url": "https://imultimod.streamlit.app/"
    },
    {
        "nombre": "Visión de la Cacería (Detección de Objetos)",
        "imagen": 'txt_to_audio.png',
        "descripcion": "El Ojo de la Cacería, capaz de detectar las siluetas de las bestias ocultas en las imágenes. Un lente YHOLO que distingue objetos para la supervivencia.",
        "enlace_texto": "YOLO: Lente Arcano",
        "url": "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/"
    },
    {
        "nombre": "Forja de Modelos Arcanos",
        "imagen": 'OIG5.jpg',
        "descripcion": "El yunque donde se entrenan las efigies mentales. Permite usar modelos previamente imbuídos con conocimiento para revelar patrones en la locura.",
        "enlace_texto": "YOLO: Entrenamiento",
        "url": "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/"
    },
    {
        "nombre": "El Canto del Cazador (Voz a Texto)",
        "imagen": 'OIG8.jpg',
        "descripcion": "Decodificación del habla en runas escritas. Captura el lamento del cazador o el susurro del Gran Ser y lo plasma en el pergamino para su estudio.",
        "enlace_texto": "Voz a Texto",
        "url": "https://traductor-ab0sp9f6fi.streamlit.app/"
    },
    {
        "nombre": "Descifrando los Tomos Prohibidos (Análisis de Datos)",
        "imagen": 'data_analisis.png',
        "descripcion": "Agentes arcanos dedicados al análisis de grandes volúmenes de datos. Permite encontrar patrones coherentes en el caos de la información de Yharnam.",
        "enlace_texto": "Análisis de Datos",
        "url": "https://asistpy-csv.streamlit.app/"
    },
    {
        "nombre": "El Susurro de la Memoria (Transcriptor)",
        "imagen": 'OIG3.jpg',
        "descripcion": "Artefacto diseñado para transcribir los largos cantos y lamentos contenidos en grabaciones de audio o video, preservando cada palabra del ritual.",
        "enlace_texto": "Transcriptor Arcano",
        "url": "https://transcript-whisper.streamlit.app/"
    },
    {
        "nombre": "Consulta del Códice (RAG/PDF)",
        "imagen": 'Chat_pdf.png',
        "descripcion": "Una aplicación que permite interrogar directamente los documentos prohibidos (PDF) utilizando la Generación Aumentada por Recuperación (RAG).",
        "enlace_texto": "RAG: Consulta del Códice",
        "url": "https://chatpdf-cc.streamlit.app/"
    },
    {
        "nombre": "El Ojo del Insight (Análisis de Imagen)",
        "imagen": 'OIG4.jpg',
        "descripcion": "Revela la capacidad de la IA para interpretar y analizar las visiones contenidas en las imágenes, incrementando nuestro nivel de 'Insight'.",
        "enlace_texto": "Vision: Revelación",
        "url": "https://vision2-gpt4o.streamlit.app/"
    },
    {
        "nombre": "Puente al Mundo Despierto (Ciberfísico)",
        "imagen": 'OIG6.jpg',
        "descripcion": "Demuestra la interacción de la lógica arcana con el mundo físico, cerrando la brecha entre el Sueño del Cazador y la realidad tangible.",
        "enlace_texto": "Ciberfísico: Interacción",
        "url": "https://vision2-gpt4o.streamlit.app/"
    },
]

# --- Renderizado de Artefactos en Columnas ---
st.markdown("### Colección de Artefactos de la Vigilia")

# Se usa un esquema de tres columnas
cols = st.columns(3)
col_index = 0

for artefacto in artefactos:
    with cols[col_index]:
        # El título de la tarjeta es el nombre gótico del artefacto
        st.markdown(f"**<h3 style='margin-top: 0px;'>{artefacto['nombre']}</h3>**", unsafe_allow_html=True)
        
        # Cargar imagen (manejo de error si no existe en el entorno)
        try:
            image = Image.open(artefacto['imagen'])
            st.image(image, use_column_width=True)
        except FileNotFoundError:
            st.image(f"https://placehold.co/200x150/1A1A2A/C0C0C0?text=Runa+Perdida", caption=f"Placeholder: {artefacto['imagen']}", use_column_width=True)
        
        # Descripción
        st.write(artefacto['descripcion'])
        
        # Enlace
        st.write(f"Acceso al Artefacto: [{artefacto['enlace_texto']}]({artefacto['url']})")

    col_index = (col_index + 1) % 3

st.markdown("---")
st.markdown("<p style='text-align: center; color: #4F4A5E;'>La cacería nunca termina.</p>", unsafe_allow_html=True)



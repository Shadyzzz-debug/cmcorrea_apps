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
    height: 100%; /* Asegura que todas las tarjetas tengan la misma altura */
}

/* Subtítulos dentro de las tarjetas (Nombres de Artefactos) */
[data-testid="stVerticalBlock"] h3 {
    color: #C0C0C0;
    border-left: 4px solid #9C7E4F; /* Acento en Bronce */
    padding-left: 10px;
    min-height: 50px; /* Estabiliza la altura del título */
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
    min-height: 90px; /* Asegura un espacio mínimo para la descripción */
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

# Diccionario para mapear URLs (simplifica la actualización)
url_updates = {
    "El Canto del Cazador (Voz a Texto)": "https://traductor-hzrluvjg4mivq7qyppstaw.streamlit.app/",
    "El Ojo del Insight (Análisis de Imagen)": "https://visionapp-gw3qmdnaf3nhnqtvpagdjp.streamlit.app/",
    "Registro de la Locura (Historial de Inferencia)": "https://histinf-2hkp6kecngkr3a7mpmjwjx.streamlit.app/",
    "Rostro de la Bestia (Reconocimiento de Dibujo)": "https://drawrecog-2jvbmiqk5np9qpyyb2azzm.streamlit.app/",
    "El Lenguaje de Yharnam (TF/IDF)": "https://9ukkeayfkfy6iesqxtzdtm.streamlit.app/",
    "Tumba Profunda (Clasificación de Texto)": "https://tdfesp-jvohc89nshr7m5jjccj9ct.streamlit.app/",
    "Análisis de Manuscritos (Procesamiento de Texto)": "https://yz3nwbxbpormlet7y3on67.streamlit.app/",
    "El Ritual del Doble Texto (tx2_analisis)": "https://abw82ihpph6gxy8ephhjux.streamlit.app/",
    "Puente al Mundo Despierto (Ciberfísico)": "https://crz7ddg7l8wb3f78ntbmla.streamlit.app/",
    "El Altar de Control (MQTT Manual)": "https://sendcmqtt-kdphuxjy7rjprdxquajky9.streamlit.app/",
    "Voz de la Runa (Control por Voz)": "https://ctrlvoice-lgppyaas3uqbshewc8ienf.streamlit.app/",
    "Morfología (Mapeo de la Palabra)": "https://66yb7na4rybehdswriewyb.streamlit.app/",
    "Escritura Antigua (OCR y Audio)": "https://ocr-audio-f5ag5fex3zxdrxv9lqckvv.streamlit.app/",
    "Consulta del Códice (RAG/PDF)": "https://chatpdf-baazt5frfiwv54xbs5tabw.streamlit.app/",
    "Manuscritos del Cazador (Handwriting)": "https://79fiqrbzsavpel4upzzi8v.streamlit.app/",
    "YOLO V5": "https://yolov5-a3dsggyrsoenznxusyrabz.streamlit.app/",
}

# --- Definición de Artefactos (Mapeo de Proyectos a la Narrativa Gótica) ---

artefactos = [
    # --- PROYECTOS ORIGINALES (TRANSCRIPCIÓN Y CLASIFICACIÓN) ---
    {
        "nombre": "Invocación de la Voz del Oráculo",
        "imagen": 'txt_to_audio2.png',
        "descripcion": "Transformación del texto escrito en un eco auditivo. Esta aplicación conjura una voz audible a partir de las runas.",
        "enlace_texto": "Texto a Voz",
        "url": "https://imultimod.streamlit.app/"
    },
    {
        "nombre": "El Canto del Cazador (Voz a Texto)",
        "imagen": 'OIG8.jpg',
        "descripcion": "Decodificación del habla en runas escritas. Captura el lamento del cazador o el susurro del Gran Ser y lo plasma en el pergamino.",
        "enlace_texto": "Voz a Texto",
        "url": "https://traductor-ab0sp9f6fi.streamlit.app/"
    },
    {
        "nombre": "El Susurro de la Memoria (Transcriptor)",
        "imagen": 'OIG3.jpg',
        "descripcion": "Artefacto diseñado para transcribir los largos cantos y lamentos contenidos en grabaciones de audio o video, preservando cada palabra.",
        "enlace_texto": "Transcriptor Arcano",
        "url": "https://transcript-whisper.streamlit.app/"
    },
    
    # --- PROYECTOS DE VISIÓN Y DETECCIÓN ---
    {
        "nombre": "Visión de la Cacería (Detección)",
        "imagen": 'txt_to_audio.png',
        "descripcion": "El Ojo de la Cacería, capaz de detectar las siluetas de las bestias ocultas en las imágenes. Un lente YHOLO para la supervivencia.",
        "enlace_texto": "YOLO: Lente Arcano",
        "url": "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/"
    },
    {
        "nombre": "Forja de Modelos Arcanos",
        "imagen": 'OIG5.jpg',
        "descripcion": "El yunque donde se entrenan las efigies mentales. Permite usar modelos imbuídos con conocimiento (YOLO) para revelar patrones en la locura.",
        "enlace_texto": "YOLO: Entrenamiento",
        "url": "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/"
    },
    {
        "nombre": "El Ojo del Insight (Análisis de Imagen)",
        "imagen": 'OIG4.jpg',
        "descripcion": "Revela la capacidad de la IA para interpretar y analizar las visiones contenidas en las imágenes, incrementando nuestro nivel de 'Insight'.",
        "enlace_texto": "Vision: Revelación",
        "url": "https://vision2-gpt4o.streamlit.app/"
    },

    # --- NUEVOS PROYECTOS DE LA CAPTURA (PROYECTOS DE DATOS Y ML) ---
    {
        "nombre": "Registro de la Locura (Historial de Inferencia)",
        "imagen": 'hist_inf.png',
        "descripcion": "Un códice que almacena y visualiza el historial de las inferencias realizadas. Es vital para rastrear la evolución de la infección en Yharnam.",
        "enlace_texto": "Hist. Inferencia",
        "url": "https://url-del-artefacto-arcano.streamlit.app/hist_inf"
    },
    {
        "nombre": "Rostro de la Bestia (Reconocimiento de Dibujo)",
        "imagen": 'drawrecog.png',
        "descripcion": "Aplica la lógica para reconocer formas y diseños trazados a mano. Útil para identificar símbolos arcanos o bocetos de criaturas.",
        "enlace_texto": "Reconocimiento",
        "url": "https://url-del-artefacto-arcano.streamlit.app/drawrecog"
    },
    {
        "nombre": "El Lenguaje de Yharnam (TF/IDF)",
        "imagen": 'TF_IDF.png',
        "descripcion": "Analiza la frecuencia y relevancia de términos en textos antiguos (Term Frequency/Inverse Document Frequency) para descifrar el léxico de los Antiguos.",
        "enlace_texto": "TF/IDF: Léxico",
        "url": "https://url-del-artefacto-arcano.streamlit.app/TF_IDF"
    },
    {
        "nombre": "Tumba Profunda (Clasificación de Texto)",
        "imagen": 'tdf_esp.png',
        "descripcion": "Mecanismo especializado en la clasificación de textos en español, separando los relatos coherentes de la locura sin forma.",
        "enlace_texto": "TDF: Clasificación",
        "url": "https://url-del-artefacto-arcano.streamlit.app/tdf_esp"
    },
    {
        "nombre": "Análisis de Manuscritos (Procesamiento de Texto)",
        "imagen": 'analisis_de_texto.png',
        "descripcion": "Herramienta fundamental para el análisis profundo de cualquier manuscrito, revelando estructura, sentimiento y patrones ocultos del texto.",
        "enlace_texto": "Análisis de Texto",
        "url": "https://url-del-artefacto-arcano.streamlit.app/analisis_de_texto"
    },
    {
        "nombre": "El Ritual del Doble Texto (tx2_analisis)",
        "imagen": 'tx2_analisis.png',
        "descripcion": "Compara dos fragmentos de pergamino o dos profecías para encontrar similitudes, divergencias o la fuente de la verdad en el caos narrativo.",
        "enlace_texto": "Análisis Comparado",
        "url": "https://url-del-artefacto-arcano.streamlit.app/tx2_analisis"
    },
    
    # --- PROYECTOS DE INTERACCIÓN Y SISTEMAS ---
    {
        "nombre": "Puente al Mundo Despierto (Ciberfísico)",
        "imagen": 'OIG6.jpg',
        "descripcion": "Demuestra la interacción de la lógica arcana con el mundo físico, cerrando la brecha entre el Sueño del Cazador y la realidad tangible.",
        "enlace_texto": "Ciberfísico: Interacción",
        "url": "https://vision2-gpt4o.streamlit.app/"
    },
    {
        "nombre": "El Altar de Control (MQTT Manual)",
        "imagen": 'send_cmqtt.png',
        "descripcion": "Control manual de sistemas remotos a través del protocolo MQTT. Envía comandos binarios y analógicos al Nexo Cósmico.",
        "enlace_texto": "Control MQTT",
        "url": "https://url-del-artefacto-arcano.streamlit.app/send_cmqtt"
    },
    {
        "nombre": "Voz de la Runa (Control por Voz)",
        "imagen": 'ctrl_voice.png',
        "descripcion": "El antiguo método de control. Ejecuta comandos sobre la realidad con la potencia de la voz, canalizada a través de la interfaz.",
        "enlace_texto": "Control Voz",
        "url": "https://url-del-artefacto-arcano.streamlit.app/ctrl_voice"
    },
    
    # --- PROYECTOS DE RECURSOS DE LENGUAJE ---
    {
        "nombre": "Morfología (Mapeo de la Palabra)",
        "imagen": 'TM.png',
        "descripcion": "Analiza la estructura de las palabras y su relación. Es el mapa de la morfología del lenguaje, esencial para entender las maldiciones.",
        "enlace_texto": "Mapeo Textual",
        "url": "https://url-del-artefacto-arcano.streamlit.app/TM"
    },
    {
        "nombre": "Escritura Antigua (OCR y Audio)",
        "imagen": 'ocr_audio.png',
        "descripcion": "Combina el reconocimiento óptico de caracteres (OCR) con el procesamiento de audio para descifrar documentos y grabaciones perdidas.",
        "enlace_texto": "OCR/Audio",
        "url": "https://url-del-artefacto-arcano.streamlit.app/ocr_audio"
    },
    {
        "nombre": "Pergamino Roto (OCR Puro)",
        "imagen": 'ocr.png',
        "descripcion": "El mecanismo base para la lectura de caracteres de imágenes estáticas. Es el primer paso para descifrar cualquier runa escrita.",
        "enlace_texto": "OCR Básico",
        "url": "https://url-del-artefacto-arcano.streamlit.app/ocr_puro"
    },
    
    # --- PROYECTOS DE PDF / RAG ---
    {
        "nombre": "Consulta del Códice (RAG/PDF)",
        "imagen": 'Chat_pdf.png',
        "descripcion": "Permite interrogar directamente los documentos prohibidos (PDF) utilizando la Generación Aumentada por Recuperación (RAG).",
        "enlace_texto": "RAG: Consulta",
        "url": "https://chatpdf-cc.streamlit.app/"
    },
    
    # --- Handwriting (NO VISTO EN LA CAPTURA, PERO COMÚN) ---
    {
        "nombre": "Manuscritos del Cazador (Handwriting)",
        "imagen": 'hand_w.png',
        "descripcion": "Sistema de reconocimiento de escritura manual, vital para interpretar las notas dejadas por cazadores caídos o mensajes crípticos.",
        "enlace_texto": "Reconocimiento HW",
        "url": "https://url-del-artefacto-arcano.streamlit.app/hand_w"
    },
    {
        "nombre": "YOLO V5",
        "imagen": 'Yolov5.png',
        "descripcion": "Versión específica del Lente Arcano YOLO. Utilizado para la detección rápida y precisa de entidades en el campo de batalla.",
        "enlace_texto": "YOLO V5 (Lente)",
        "url": "https://url-del-artefacto-arcano.streamlit.app/Yolov5"
    },
]

# Aplicar las actualizaciones de URL
for artefacto in artefactos:
    if artefacto["nombre"] in url_updates:
        artefacto["url"] = url_updates[artefacto["nombre"]]

# Configuración del ciclo de imágenes
image_cycle = ['pipi.png', 'fifi.png', 'lili.png']

# --- Renderizado de Artefactos en Columnas ---
st.markdown("### Colección de Artefactos de la Vigilia")

# Se usa un esquema de tres columnas
cols = st.columns(3)
num_columns = 3
col_index = 0

for i, artefacto in enumerate(artefactos):
    # Asignar imagen del ciclo
    image_file = image_cycle[i % len(image_cycle)]
    
    # Se añade un espacio antes del with cols[col_index] para manejar las columnas.
    col = cols[col_index]
    
    with col:
        # El título de la tarjeta es el nombre gótico del artefacto
        st.markdown(f"**<h3 style='margin-top: 0px;'>{artefacto['nombre']}</h3>**", unsafe_allow_html=True)
        
        # Cargar imagen (manejo de error si no existe en el entorno)
        try:
            # Comentario para indicar dónde va la imagen real
            # Imagen Placeholder: <nombre_archivo_sugerido>.png
            st.markdown(f"<!-- Imagen Placeholder: {image_file} -->")
            image = Image.open(artefacto['imagen'])
            st.image(image, use_column_width=True)
        except FileNotFoundError:
            # Mostrar el placeholder con el nombre de archivo sugerido (pipi.png, fifi.png, lili.png)
            st.image(f"https://placehold.co/200x150/1A1A2A/C0C0C0?text=Remplazar:+{image_file}", caption=f"Remplazar por: {image_file}", use_column_width=True)
        
        # Descripción
        st.write(artefacto['descripcion'])
        
        # Enlace
        st.write(f"Acceso al Artefacto: [{artefacto['enlace_texto']}]({artefacto['url']})")

    col_index = (col_index + 1) % num_columns

st.markdown("---")
st.markdown("<p style='text-align: center; color: #4F4A5E;'>La cacería nunca termina.</p>", unsafe_allow_html=True)



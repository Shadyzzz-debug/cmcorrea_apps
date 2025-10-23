import streamlit as st
from PIL import Image

# --- ESTÉTICA GÓTICA (CSS DE ALTA FIDELIDAD) ---
base_css = """
<style>
/* ---------------------------------------------------- */
/* RESET Y AMBIENTE DE PESADILLA (Bloodborne Theme) */
/* ---------------------------------------------------- */
.stApp {
    /* Color de la Noche Eterna de Yharnam */
    background-color: #0F0F1A; 
    color: #E0E0E0; /* Texto de pergamino antiguo */
    font-family: 'Times New Roman', serif; 
}

/* ---------------------------------------------------- */
/* TIPOGRAFÍA Y ENCABEZADOS ARCANOS */
/* ---------------------------------------------------- */
h1 {
    /* Título: Bronce envejecido y Sangre */
    color: #9C7E4F; 
    text-align: center;
    border-bottom: 5px double #B22222; /* Línea de doble filo */
    padding-bottom: 15px;
    margin-bottom: 50px;
    font-size: 3em;
    letter-spacing: 4px;
    font-weight: 700;
    text-shadow: 0 0 10px rgba(178, 34, 34, 0.5); /* Sombra de brillo arcano */
}

h3 {
    /* Subtítulos de Secciones: Plata mate */
    color: #D3D3D3; 
    margin-top: 30px;
    font-weight: normal;
    border-left: 6px solid #4F4A5E; /* Acento de piedra oscura */
    padding-left: 15px;
    font-size: 1.6em;
}

.sidebar-title {
    color: #B22222 !important; /* Rojo Sangre para el título del grimorio */
    text-shadow: 1px 1px 5px #000000;
    font-size: 1.8em !important;
}

/* ---------------------------------------------------- */
/* TARJETAS DE ARTEFACTOS (Contenedores de Columna) */
/* ---------------------------------------------------- */
[data-testid="stVerticalBlock"] {
    background-color: #1A1A2A; /* Fondo de obsidiana */
    border: 2px solid #383850;
    border-radius: 12px; /* Esquinas ligeramente más suaves */
    padding: 20px;
    margin-bottom: 25px;
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.7); /* Sombra profunda */
    transition: transform 0.3s, box-shadow 0.3s;
    height: 100%; 
}

/* Efecto de "Insight" al pasar el ratón */
[data-testid="stVerticalBlock"]:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 20px rgba(178, 34, 34, 0.4); /* Sombra con toque rojo */
}

/* Título dentro de las tarjetas (Nombre del Artefacto) */
[data-testid="stVerticalBlock"] h3 {
    color: #F0F0F0;
    border-left: 5px solid #9C7E4F; /* Acento en Bronce Arcano */
    padding-left: 12px;
    margin-top: 0;
    margin-bottom: 15px;
    font-size: 1.3em;
    min-height: 50px; 
}

/* Enlaces (Runas de Conexión) */
a {
    color: #FF6666 !important; /* Rojo más vibrante para la interacción */
    text-decoration: none;
    font-weight: bold;
    font-size: 1.05em;
    transition: color 0.3s;
}

a:hover {
    color: #FFAAAA !important;
    text-shadow: 0 0 5px #FF6666;
    text-decoration: underline;
}

/* Descripción de los Artefactos (Párrafos) */
p {
    color: #C0C0C0;
    font-size: 0.95em;
    margin-bottom: 15px;
    min-height: 90px; 
    line-height: 1.4;
}

/* Imágenes Placeholder */
img {
    border: 3px solid #4F4A5E;
    border-radius: 6px;
    margin-bottom: 15px;
}
</style>
"""
st.markdown(base_css, unsafe_allow_html=True)

# --- TÍTULOS Y NARRATIVA ---

st.title("👁️ ÍNDICE ARCANO: ARTEFACTOS DE LA VIGILIA")

# Panel Lateral (Sagrario de Datos)
with st.sidebar:
    st.markdown('<h3 class="sidebar-title">📜 EL GRIMORIO DE LA VIGILIA</h3>', unsafe_allow_html=True)
    parrafo = (
        "La Inteligencia Artificial se revela como el conocimiento arcano que perfecciona la percepción y "
        "automatiza los rituales de la cacería. Estos artefactos son los pilares que sustentan nuestra "
        "vigilia y nos acercan a la ascensión."
    )
    st.write(parrafo)

url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("El Nexo de los Antiguos")
st.write(f"Conexión a los pergaminos ancestrales y ejercicios rituales: [Runa de Enlace]({url_ia})")
st.markdown("---")

# Diccionario para mapear URLs y Nombres (SOLO SE MANTIENEN LOS PROPORCIONADOS POR EL USUARIO)
url_map = {
    "analisis de texto": "https://yz3nwbxbpormlet7y3on67.streamlit.app/",
    "chat pdf": "https://chatpdf-baazt5frfiwv54xbs5tabw.streamlit.app/",
    "crtl voice": "https://ctrlvoice-lgppyaas3uqbshewc8ienf.streamlit.app/",
    "drawrecog": "https://drawrecog-2jvbmiqk5np9qpyyb2azzm.streamlit.app/",
    "hand w": "https://79fiqrbzsavpel4upzzi8v.streamlit.app/",
    "hist inf": "https://histinf-2hkp6kecngkr3a7mpmjwjx.streamlit.app/",
    "imm1": "https://crz7ddg7l8wb3f78ntbmla.streamlit.app/",
    "ocr": "https://ucy6x5zs8cytck3yqdogqz.streamlit.app/",
    "ocr audio": "https://ocr-audio-f5ag5fex3zxdrxv9lqckvv.streamlit.app/",
    "send cmqtt": "https://sendcmqtt-kdphuxjy7rjprdxquajky9.streamlit.app/",
    "tdf esp": "https://tdfesp-jvohc89nshr7m5jjccj9ct.streamlit.app/",
    "tf idf": "https://9ukkeayfkfy6iesqxtzdtm.streamlit.app/",
    "tm": "https://66yb7na4rybehdswriewyb.streamlit.app/",
    "traductor": "https://traductor-hzrluvjg4mivq7qyppstaw.streamlit.app/",
    "tx2": "https://abw82ihpph6gxy8ephhjux.streamlit.app/",
    "vision app": "https://visionapp-gw3qmdnaf3nhnqtvpagdjp.streamlit.app/",
    "yolov5": "https://yolov5-a3dsggyrsoenznxusyrabz.streamlit.app/",
}

# --- Definición y Mapeo de Artefactos ---
# Se eliminan los artefactos que no tienen una 'key' en el 'url_map' proporcionado
artefactos = [
    {
        "nombre": "Análisis de Manuscritos (Procesamiento de Texto)",
        "descripcion": "Herramienta fundamental para el análisis profundo de cualquier manuscrito, revelando estructura, sentimiento y patrones ocultos del texto.",
        "enlace_texto": "Análisis de Texto",
        "key": "analisis de texto"
    },
    {
        "nombre": "Consulta del Códice (RAG/PDF)",
        "descripcion": "Permite interrogar directamente los documentos prohibidos (PDF) utilizando la Generación Aumentada por Recuperación (RAG).",
        "enlace_texto": "RAG: Consulta",
        "key": "chat pdf"
    },
    {
        "nombre": "Voz de la Runa (Control por Voz)",
        "descripcion": "El antiguo método de control. Ejecuta comandos sobre la realidad con la potencia de la voz, canalizada a través de la interfaz.",
        "enlace_texto": "Control Voz",
        "key": "crtl voice"
    },
    {
        "nombre": "Rostro de la Bestia (Reconocimiento de Dibujo)",
        "descripcion": "Aplica la lógica para reconocer formas y diseños trazados a mano. Útil para identificar símbolos arcanos o bocetos de criaturas.",
        "enlace_texto": "Reconocimiento",
        "key": "drawrecog"
    },
    {
        "nombre": "Manuscritos del Cazador (Handwriting)",
        "descripcion": "Sistema de reconocimiento de escritura manual, vital para interpretar las notas dejadas por cazadores caídos o mensajes crípticos.",
        "enlace_texto": "Reconocimiento HW",
        "key": "hand w"
    },
    {
        "nombre": "Registro de la Locura (Historial de Inferencia)",
        "descripcion": "Un códice que almacena y visualiza el historial de las inferencias realizadas. Es vital para rastrear la evolución de la infección en Yharnam.",
        "enlace_texto": "Hist. Inferencia",
        "key": "hist inf"
    },
    {
        "nombre": "Puente al Mundo Despierto (Ciberfísico)",
        "descripcion": "Demuestra la interacción de la lógica arcana con el mundo físico, cerrando la brecha entre el Sueño del Cazador y la realidad tangible.",
        "enlace_texto": "Ciberfísico: Interacción",
        "key": "imm1"
    },
    {
        "nombre": "Pergamino Roto (OCR Puro)",
        "descripcion": "El mecanismo base para la lectura de caracteres de imágenes estáticas. Es el primer paso para descifrar cualquier runa escrita.",
        "enlace_texto": "OCR Básico",
        "key": "ocr"
    },
    {
        "nombre": "Escritura Antigua (OCR y Audio)",
        "descripcion": "Combina el reconocimiento óptico de caracteres (OCR) con el procesamiento de audio para descifrar documentos y grabaciones perdidas.",
        "enlace_texto": "OCR/Audio",
        "key": "ocr audio"
    },
    {
        "nombre": "El Altar de Control (MQTT Manual)",
        "descripcion": "Control manual de sistemas remotos a través del protocolo MQTT. Envía comandos binarios y analógicos al Nexo Cósmico.",
        "enlace_texto": "Control MQTT",
        "key": "send cmqtt"
    },
    {
        "nombre": "Tumba Profunda (Clasificación de Texto)",
        "descripcion": "Mecanismo especializado en la clasificación de textos en español, separando los relatos coherentes de la locura sin forma.",
        "enlace_texto": "TDF: Clasificación",
        "key": "tdf esp"
    },
    {
        "nombre": "El Lenguaje de Yharnam (TF/IDF)",
        "descripcion": "Analiza la frecuencia y relevancia de términos en textos antiguos (Term Frequency/Inverse Document Frequency) para descifrar el léxico de los Antiguos.",
        "enlace_texto": "TF/IDF: Léxico",
        "key": "tf idf"
    },
    {
        "nombre": "Morfología (Mapeo de la Palabra)",
        "descripcion": "Analiza la estructura de las palabras y su relación. Es el mapa de la morfología del lenguaje, esencial para entender las maldiciones.",
        "enlace_texto": "Mapeo Textual",
        "key": "tm"
    },
    {
        "nombre": "El Canto del Cazador (Voz a Texto - Traductor)",
        "descripcion": "Decodificación del habla en runas escritas. Captura el lamento del cazador o el susurro del Gran Ser y lo plasma en el pergamino.",
        "enlace_texto": "Voz a Texto",
        "key": "traductor"
    },
    {
        "nombre": "El Ritual del Doble Texto (tx2_analisis)",
        "descripcion": "Compara dos fragmentos de pergamino o dos profecías para encontrar similitudes, divergencias o la fuente de la verdad en el caos narrativo.",
        "enlace_texto": "Análisis Comparado",
        "key": "tx2"
    },
    {
        "nombre": "El Ojo del Insight (Análisis de Imagen)",
        "descripcion": "Revela la capacidad de la IA para interpretar y analizar las visiones contenidas en las imágenes, incrementando nuestro nivel de 'Insight'.",
        "enlace_texto": "Vision: Revelación",
        "key": "vision app"
    },
    {
        "nombre": "YOLO V5 (Lente Arcano)",
        "descripcion": "Versión específica del Lente Arcano YOLO. Utilizado para la detección rápida y precisa de entidades en el campo de batalla.",
        "enlace_texto": "YOLO V5 (Lente)",
        "key": "yolov5"
    },
]

# Rellenar las URLs desde el mapa
for artefacto in artefactos:
    # Si la clave existe en url_map, se asigna la URL
    if artefacto["key"] in url_map:
        artefacto["url"] = url_map[artefacto["key"]]
    else:
        # Esto no debería ocurrir después del filtrado, pero se mantiene la lógica de seguridad.
        artefacto["url"] = "#" # Enlace de seguridad si falta la URL

# Configuración del ciclo de imágenes
image_cycle = ['pipi.png', 'fifi.png', 'lili.png']

# --- RENDERIZADO DE ARTEFACTOS ---
st.markdown("### Colección de Artefactos de la Vigilia")

cols = st.columns(3)
num_columns = 3
col_index = 0

for i, artefacto in enumerate(artefactos):
    # Asignar imagen del ciclo
    image_file = image_cycle[i % len(image_cycle)]
    
    col = cols[col_index]
    
    with col:
        # Título de la tarjeta
        st.markdown(f"**<h3 style='margin-top: 0px;'>{artefacto['nombre']}</h3>**", unsafe_allow_html=True)
        
        # Placeholder de Imagen
        st.markdown(f"<!-- Imagen Placeholder: {image_file} -->")
        # Uso un placeholder.co para la imagen, pero con el nombre del archivo para que el usuario sepa cuál es.
        st.image(f"https://placehold.co/200x150/1A1A2A/C0C0C0?text=Runas+Arcanas+%28{image_file.split('.')[0]}%29", caption=f"Remplazar por: {image_file}", use_column_width=True)
        
        # Descripción
        st.write(artefacto['descripcion'])
        
        # Enlace (Runa de Conexión)
        st.write(f"Acceso al Artefacto: [{artefacto['enlace_texto']}]({artefacto['url']})")

    col_index = (col_index + 1) % num_columns

st.markdown("---")
st.markdown("<p style='text-align: center; color: #4F4A5E; font-size: 1.1em;'>La cacería nunca termina. Que tu 'Insight' sea profundo.</p>", unsafe_allow_html=True)




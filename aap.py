import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(
    page_title="Atenas & Meteora (Familia Tejedor Cubo by JC)",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Estilo CSS personalizado
st.markdown("""
    <style>
    .main {
        background-color: #0a0a0a;
        color: #f5f2ed;
    }
    .stButton>button {
        width: 100%;
        border-radius: 0px;
        border: 1px solid #c5a059;
        background-color: transparent;
        color: #c5a059;
    }
    .stButton>button:hover {
        background-color: #c5a059;
        color: #0a0a0a;
    }
    h1, h2, h3 {
        font-family: 'serif';
        color: #c5a059;
    }
    .day-card {
        border: 1px solid rgba(197, 160, 89, 0.2);
        padding: 20px;
        margin-bottom: 20px;
        background-color: rgba(255, 255, 255, 0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# Datos del Itinerario
ITINERARY = [
    {
        "day": 1,
        "date": "Jueves 2 de abril",
        "title": "Aterrizaje en la Historia",
        "emoji": "✈️",
        "location": "Atenas",
        "hero_image": "https://github.com/josecarlostejedor/AtenasJC/blob/main/aterrizaje.jpg?raw=true",
        "activities": [
            {"time": "Tarde", "title": "Llegada al Aeropuerto de Atenas", "desc": "Traslado al hotel en Koukaki."},
            {"time": "Atardecer", "title": "Paseo por Dionysiou Areopagitou", "desc": "La calle peatonal más bonita de Atenas."},
            {"time": "Noche", "title": "Cena en el barrio de Psirí", "desc": "Ambiente animado con tabernas tradicionales."}
        ]
    },
    {
        "day": 2,
        "date": "Viernes 3 de abril",
        "title": "El Oráculo de Delfos",
        "emoji": "🏛️",
        "location": "Delfos · Arachova",
        "hero_image": "https://github.com/josecarlostejedor/AtenasJC/blob/main/oraculodelfos.jpg?raw=true",
        "activities": [
            {"time": "08:00", "title": "Salida hacia Delfos", "desc": "Recoge el coche de alquiler."},
            {"time": "10:30", "title": "Santuario de Apolo", "desc": "El centro del mundo antiguo."},
            {"time": "21:00", "title": "Procesión del Epitafios", "desc": "Viernes Santo Ortodoxo."}
        ]
    },
    {
        "day": 3,
        "date": "Sábado 4 de abril",
        "title": "Tesoros y Vida Bohemia",
        "emoji": "🏺",
        "location": "Atenas",
        "hero_image": "https://github.com/josecarlostejedor/AtenasJC/blob/main/tesoroyvidabohemia.jpg?raw=true",
        "activities": [
            {"time": "09:00", "title": "Museo Arqueológico Nacional", "desc": "La 'caja fuerte' de Grecia."},
            {"time": "12:30", "title": "Barrio de Exarchia", "desc": "El corazón intelectual y rebelde."},
            {"time": "00:00", "title": "Misa de Resurrección", "desc": "Christos Anesti!"}
        ]
    },
    {
        "day": 4,
        "date": "Domingo 5 de abril",
        "title": "El Milagro de Meteora",
        "emoji": "⛰️",
        "location": "Meteora · Kastraki",
        "hero_image": "https://github.com/josecarlostejedor/AtenasJC/blob/main/meteora.jpg?raw=true",
        "activities": [
            {"time": "06:00", "title": "Salida hacia Meteora", "desc": "Son ~4 horas de camino."},
            {"time": "10:30", "title": "Gran Meteoro", "desc": "El más grande de los monasterios."},
            {"time": "14:30", "title": "Comida de Pascua", "desc": "El gran día del cordero al espiedo."}
        ]
    },
    {
        "day": 5,
        "date": "Lunes 6 de abril",
        "title": "El Corazón de la Civilización",
        "emoji": "🏛️",
        "location": "Atenas — Acrópolis",
        "hero_image": "https://github.com/josecarlostejedor/AtenasJC/blob/main/corazon.jpg?raw=true",
        "activities": [
            {"time": "08:00", "title": "Acrópolis", "desc": "Entra puntual a las 8:00."},
            {"time": "10:30", "title": "Museo de la Acrópolis", "desc": "Las Cariátides originales."},
            {"time": "17:00", "title": "Mercado de Monastiraki", "desc": "Freddo Espresso time."}
        ]
    },
    {
        "day": 6,
        "date": "Martes 7 de abril",
        "title": "Despedida con Honor",
        "emoji": "👋",
        "location": "Atenas → Madrid",
        "hero_image": "https://github.com/josecarlostejedor/AtenasJC/blob/main/despedida.jpg?raw=true",
        "activities": [
            {"time": "09:00", "title": "Estadio Panatenaico", "desc": "Construido íntegramente en mármol."},
            {"time": "11:00", "title": "Cambio de Guardia", "desc": "Plaza Syntagma."},
            {"time": "Tarde", "title": "Vuelo de regreso", "desc": "Traslado al aeropuerto."}
        ]
    }
]

# Sidebar
st.sidebar.title("🏛️ Atenas & Meteora")
st.sidebar.markdown("(Familia Tejedor Cubo by JC)")
st.sidebar.markdown("---")
day_titles = [f"Día {d['day']}: {d['title']}" for d in ITINERARY]
selected_day_index = st.sidebar.radio("Ir al día:", range(len(day_titles)), format_func=lambda x: day_titles[x])

# Main Content
st.title("Atenas & Meteora")
st.markdown("### (Familia Tejedor Cubo by JC)")
st.subheader("Semana Santa 2026 · Itinerario de Viaje")

# Display Selected Day
day = ITINERARY[selected_day_index]
st.markdown(f"## {day['emoji']} Día {day['day']}: {day['title']}")
st.markdown(f"**{day['date']}** · 📍 {day['location']}")

st.image(day['hero_image'], use_container_width=True)

st.markdown("### Actividades")
for act in day['activities']:
    with st.container():
        st.markdown(f"""
        <div class="day-card">
            <span style="color: #c5a059; font-weight: bold;">{act['time']}</span><br/>
            <span style="font-size: 1.2em; font-weight: bold;">{act['title']}</span><br/>
            <span style="color: rgba(245, 242, 237, 0.7);">{act['desc']}</span>
        </div>
        """, unsafe_allow_html=True)

# Summary Table
st.markdown("---")
st.markdown("### Resumen del Viaje")
df = pd.DataFrame([
    {"Día": d['day'], "Fecha": d['date'], "Ubicación": d['location'], "Título": d['title']}
    for d in ITINERARY
])
st.table(df)

# Footer
st.markdown("---")
st.markdown("Viaje de Madrid a Atenas · Semana Santa 2026 · App por JC Tejedor")

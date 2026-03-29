from flask import Flask, render_template_string
import json

app = Flask(__name__)

ITINERARY = [
    {
        "day": 1,
        "date": "Jueves 2 de abril",
        "title": "Aterrizaje en la Historia",
        "emoji": "✈️",
        "color": "#C9A84C",
        "location": "Atenas",
        "hero_image": "https://images.unsplash.com/photo-1603565816030-6b389eeb23cb?w=1200&q=80",
        "map_query": "Dionysiou+Areopagitou,+Athens,+Greece",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3145.6!2d23.7239!3d37.9707!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x14a1bd1f3e23a3c7%3A0x3!2sDionysiou+Areopagitou!5e0!3m2!1ses!2ses!4v1",
        "activities": [
            {
                "time": "Tarde",
                "icon": "🛬",
                "title": "Llegada al Aeropuerto de Atenas",
                "description": "Traslado al hotel en el barrio de Koukaki, al sur de la Acrópolis. Más auténtico y tranquilo que el centro.",
                "tip": "Koukaki es ideal: mezcla perfecta de autenticidad y comodidad.",
                "links": [
                    {"label": "Aeropuerto de Atenas", "url": "https://www.aia.gr/"},
                    {"label": "Barrio Koukaki", "url": "https://maps.app.goo.gl/koukaki"}
                ]
            },
            {
                "time": "Atardecer",
                "icon": "🚶",
                "title": "Paseo por Dionysiou Areopagitou",
                "description": "La calle peatonal más bonita de Atenas rodea la falda de la Acrópolis. El Partenón se ilumina al caer la noche.",
                "tip": "Llega sobre las 19:30 para ver el atardecer dorado sobre el mármol.",
                "links": [
                    {"label": "Ver en Google Maps", "url": "https://maps.app.goo.gl/dionysiou"},
                    {"label": "Guía de la zona", "url": "https://www.visitgreece.gr/athens/"}
                ]
            },
            {
                "time": "Noche",
                "icon": "🍽️",
                "title": "Cena en el barrio de Psirí",
                "description": "Ambiente animado con tabernas tradicionales. Busca la taberna Lithos para comida excelente o Little Kook para un café con decoración extravagante.",
                "tip": "Little Kook cambia su decoración cada temporada. ¡Una experiencia única!",
                "links": [
                    {"label": "Taberna Lithos", "url": "https://www.google.com/maps/search/Lithos+Psiri+Athens"},
                    {"label": "Little Kook Athens", "url": "https://www.google.com/maps/search/Little+Kook+Athens"}
                ]
            }
        ]
    },
    {
        "day": 2,
        "date": "Viernes 3 de abril",
        "title": "El Oráculo de Delfos",
        "emoji": "🏛️",
        "color": "#5C8A6B",
        "location": "Delfos · Arachova · Atenas",
        "hero_image": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&q=80",
        "map_query": "Delphi+Archaeological+Site,+Greece",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d12734.1!2d22.5011!3d38.4824!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x135c8d90bde8647f%3A0x1!2sDelphi!5e0!3m2!1ses!2ses!4v1",
        "activities": [
            {
                "time": "08:00",
                "icon": "🚗",
                "title": "Salida hacia Delfos",
                "description": "Recoge el coche de alquiler y pon rumbo a Delfos (2.5h). La carretera por el Parnaso es espectacular.",
                "tip": "Alquila el coche la tarde anterior para salir sin perder tiempo.",
                "links": [
                    {"label": "Ruta en Google Maps", "url": "https://www.google.com/maps/dir/Athens/Delphi,+Greece"},
                    {"label": "Alquiler de coches Atenas", "url": "https://www.discovercars.com/greece/athens"}
                ]
            },
            {
                "time": "10:30",
                "icon": "🏛️",
                "title": "Santuario de Apolo en Delfos",
                "description": "El centro del mundo antiguo. Visita el Teatro, el Estadio y baja al Tholos de Atenea Pronaia (el templo circular). En el Museo, el Auriga de Bronce es impresionante: fíjate en sus pestañas.",
                "tip": "Compra la entrada combinada (yacimiento + museo). Son 12€. El museo es imprescindible.",
                "links": [
                    {"label": "Entradas oficiales", "url": "https://etickets.tap.gr/"},
                    {"label": "Info Delfos", "url": "https://odysseus.culture.gr/h/3/gh351.jsp?obj_id=2507"}
                ]
            },
            {
                "time": "14:00",
                "icon": "🧀",
                "title": "Almuerzo en Arachova",
                "description": "El pueblo de montaña más bonito de Grecia central. Prueba el queso Formaela a la plancha y el vino local. Un lujo gastronómico.",
                "tip": "Formaela es una IGP griega. Solo se produce aquí. No te lo pierdas.",
                "links": [
                    {"label": "Arachova en Maps", "url": "https://www.google.com/maps/search/Arachova+Greece"}
                ]
            },
            {
                "time": "21:00",
                "icon": "🕯️",
                "title": "Procesión del Epitafios (Viernes Santo Ortodoxo)",
                "description": "Ve a la Catedral Metropolitana (Mitropoli) para ver la procesión. Miles de velas amarillas en silencio. De los momentos más emocionantes del año en Atenas.",
                "tip": "Lleva una vela. Te la ofrecerán en la entrada de la iglesia.",
                "links": [
                    {"label": "Catedral Metropolitana", "url": "https://www.google.com/maps/search/Metropolitan+Cathedral+Athens"}
                ]
            }
        ]
    },
    {
        "day": 3,
        "date": "Sábado 4 de abril",
        "title": "Tesoros y Vida Bohemia",
        "emoji": "🏺",
        "color": "#8B4A6B",
        "location": "Atenas",
        "hero_image": "https://images.unsplash.com/photo-1555993539-1732b0258235?w=1200&q=80",
        "map_query": "National+Archaeological+Museum+Athens",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3144.5!2d23.7312!3d37.9836!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x14a1bd3e7b13c4cd%3A0x1!2sNational+Archaeological+Museum!5e0!3m2!1ses!2ses!4v1",
        "activities": [
            {
                "time": "09:00",
                "icon": "🏺",
                "title": "Museo Arqueológico Nacional",
                "description": "La 'caja fuerte' de Grecia. Busca el Mecanismo de Anticitera (el primer ordenador de la historia, 100 a.C.) y la Máscara de Agamenón en oro macizo.",
                "tip": "Llega justo a la apertura para evitar grupos. Reserva al menos 2.5 horas.",
                "links": [
                    {"label": "Web oficial del Museo", "url": "https://www.namuseum.gr/"},
                    {"label": "Reservar entradas", "url": "https://etickets.tap.gr/"}
                ]
            },
            {
                "time": "12:30",
                "icon": "✊",
                "title": "Barrio de Exarchia",
                "description": "El corazón intelectual y rebelde de Atenas. Grafitis de museo, librerías de segunda mano y la mejor música alternativa. Un universo paralelo a la Atenas turística.",
                "tip": "Es un barrio progresista y seguro. Perfecto para tomar café y observar.",
                "links": [
                    {"label": "Exarchia en Maps", "url": "https://www.google.com/maps/search/Exarchia+Athens"}
                ]
            },
            {
                "time": "18:00",
                "icon": "🌅",
                "title": "Atardecer en el Monte Licabeto",
                "description": "El punto más alto de Atenas. Vista de 360° sobre toda la cuenca del Ática. El teleférico te sube en minutos.",
                "tip": "Hay teleférico (recomendado para la bajada, ya que la subida a pie son 20 min amenos).",
                "links": [
                    {"label": "Monte Licabeto", "url": "https://www.google.com/maps/search/Lycabettus+Hill+Athens"},
                    {"label": "Teleférico Licabeto", "url": "https://www.lycabettushill.com/"}
                ]
            },
            {
                "time": "00:00",
                "icon": "✨",
                "title": "Misa de Resurrección — Christos Anesti",
                "description": "El momento más alegre del año en Grecia. En cualquier iglesia de Plaka, a medianoche todos encienden su vela y se saludan '¡Christos Anesti!' (Cristo ha resucitado). Fuegos artificiales, canto y emoción.",
                "tip": "La iglesia de Agios Georgios en la cima del Licabeto tiene la misa más espectacular.",
                "links": [
                    {"label": "Iglesias de Plaka", "url": "https://www.google.com/maps/search/church+Plaka+Athens"}
                ]
            }
        ]
    },
    {
        "day": 4,
        "date": "Domingo 5 de abril",
        "title": "El Milagro de Meteora",
        "emoji": "⛰️",
        "color": "#4A7BAE",
        "location": "Meteora · Kastraki",
        "hero_image": "https://images.unsplash.com/photo-1534430480872-3498386e7856?w=1200&q=80",
        "map_query": "Meteora,+Greece",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d25456.2!2d21.6306!3d39.7217!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x135893b8ae5f7f97%3A0x1!2sMeteora!5e0!3m2!1ses!2ses!4v1",
        "activities": [
            {
                "time": "06:00",
                "icon": "🚗",
                "title": "Salida madrugadora hacia Meteora",
                "description": "Son ~4 horas de camino. Sale muy temprano para aprovechar el día. Alternativa: tren nocturno o tour privado con minibús.",
                "tip": "El tren Atenas-Kalambaka es una opción relajante y pintoresca (~4.5h). Hay salidas tempranas.",
                "links": [
                    {"label": "Ruta en coche", "url": "https://www.google.com/maps/dir/Athens/Meteora"},
                    {"label": "Trenes Hellenic Train", "url": "https://www.hellenictrain.gr/"}
                ]
            },
            {
                "time": "10:30",
                "icon": "⛪",
                "title": "Gran Meteoro — Monasterio de la Transfiguración",
                "description": "El más grande e importante de los monasterios. Fundado en el siglo XIV. Las vistas desde arriba quitan el aliento.",
                "tip": "Dress code obligatorio: rodillas y hombros cubiertos. Hay pañuelos disponibles en la entrada.",
                "links": [
                    {"label": "Horarios monasterios", "url": "https://www.meteora.gr/"},
                    {"label": "Gran Meteoro en Maps", "url": "https://www.google.com/maps/search/Great+Meteoron+Monastery"}
                ]
            },
            {
                "time": "12:00",
                "icon": "🌸",
                "title": "Monasterio de Roussanou",
                "description": "Regentado por monjas. El más fotogénico por su posición y sus jardines en flor. Las vistas desde su terraza son las más dramáticas de Meteora.",
                "tip": "Roussanou está en un peñasco casi inaccesible. El acceso es por un puente de madera sobre el vacío.",
                "links": [
                    {"label": "Roussanou en Maps", "url": "https://www.google.com/maps/search/Roussanou+Monastery+Meteora"}
                ]
            },
            {
                "time": "14:30",
                "icon": "🍖",
                "title": "Comida de Pascua en Kastraki",
                "description": "Hoy es el gran día del cordero al espiedo. Come en una taberna del pueblo de Kastraki. Verás a familias griegas celebrando en la calle. Es la Grecia más real.",
                "tip": "Reserva la noche anterior. Es Pascua y las tabernas se llenan de locales.",
                "links": [
                    {"label": "Restaurantes Kastraki", "url": "https://www.google.com/maps/search/restaurant+Kastraki+Meteora"},
                    {"label": "Pueblo de Kastraki", "url": "https://www.google.com/maps/search/Kastraki+village+Greece"}
                ]
            }
        ]
    },
    {
        "day": 5,
        "date": "Lunes 6 de abril",
        "title": "El Corazón de la Civilización",
        "emoji": "🏛️",
        "color": "#A0522D",
        "location": "Atenas — Acrópolis",
        "hero_image": "https://images.unsplash.com/photo-1555993539-1732b0258235?w=1200&q=80",
        "map_query": "Acropolis+of+Athens,+Greece",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3145.9!2d23.7257!3d37.9715!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x14a1bd1f9b64f9f1%3A0x1!2sAcropolis+of+Athens!5e0!3m2!1ses!2ses!4v1",
        "activities": [
            {
                "time": "08:00",
                "icon": "🏛️",
                "title": "Acrópolis — En la apertura",
                "description": "Entra puntual a las 8:00. Sube por la entrada del Teatro de Dioniso. Además del Partenón, busca el Erecteion y sus Cariátides (columnas con forma de mujer). Son las más fotografiadas del mundo.",
                "tip": "Las primeras 2 horas son las mejores: luz dorada, pocos turistas y silencio.",
                "links": [
                    {"label": "Entradas Acrópolis", "url": "https://etickets.tap.gr/"},
                    {"label": "Info oficial", "url": "https://www.theacropolismuseum.gr/"}
                ]
            },
            {
                "time": "10:30",
                "icon": "🏺",
                "title": "Museo de la Acrópolis",
                "description": "Diseño arquitectónico impresionante. Las Cariátides originales están aquí (las que ves arriba son copias). La cafetería tiene vistas directas al Partenón. Almuerza aquí.",
                "tip": "El suelo de cristal del museo deja ver las excavaciones originales bajo tus pies.",
                "links": [
                    {"label": "Museo de la Acrópolis", "url": "https://www.theacropolismuseum.gr/"},
                    {"label": "Reservar entradas", "url": "https://etickets.tap.gr/"}
                ]
            },
            {
                "time": "15:00",
                "icon": "🏘️",
                "title": "Anafiótika — El barrio-isla",
                "description": "Un rincón secreto en la ladera de la Acrópolis que parece una isla de las Cícladas. Casitas blancas, gatos y silencio total. Un secreto dentro de la ciudad.",
                "tip": "Muy pocas personas saben de este barrio. Es el contraste perfecto con el caos turístico de Plaka.",
                "links": [
                    {"label": "Anafiótika en Maps", "url": "https://www.google.com/maps/search/Anafiotika+Athens"}
                ]
            },
            {
                "time": "17:00",
                "icon": "🛍️",
                "title": "Mercado de Monastiraki y Freddo Espresso",
                "description": "El mercado de pulgas más famoso de Atenas. Antigüedades, especias y recuerdos. Pide un 'Freddo Espresso' (café con hielo batido): es la bebida nacional moderna de los griegos.",
                "tip": "El Freddo Espresso se pide sin azúcar. Si quieres dulce, di 'glikó'. Es diferente al café frappé.",
                "links": [
                    {"label": "Mercado Monastiraki", "url": "https://www.google.com/maps/search/Monastiraki+flea+market+Athens"}
                ]
            }
        ]
    },
    {
        "day": 6,
        "date": "Martes 7 de abril",
        "title": "Despedida con Honor",
        "emoji": "👋",
        "color": "#6B5C8A",
        "location": "Atenas → Madrid",
        "hero_image": "https://images.unsplash.com/photo-1603565816030-6b389eeb23cb?w=1200&q=80",
        "map_query": "Panathenaic+Stadium+Athens",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3146.4!2d23.7412!3d37.9682!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x14a1bd29e6bbec1f%3A0x1!2sPanathenaic+Stadium!5e0!3m2!1ses!2ses!4v1",
        "activities": [
            {
                "time": "09:00",
                "icon": "🏟️",
                "title": "Estadio Panatenaico",
                "description": "El único estadio del mundo construido íntegramente en mármol blanco. Aquí nacieron los Juegos Olímpicos modernos en 1896. Puedes correr en la pista y llegar a la meta olímpica.",
                "tip": "La entrada incluye audioguía. Solo son 5€ y merece mucho la pena.",
                "links": [
                    {"label": "Estadio Panatenaico", "url": "https://www.panathenaicstadium.gr/"},
                    {"label": "Horarios y entradas", "url": "https://www.panathenaicstadium.gr/visit/"}
                ]
            },
            {
                "time": "10:00",
                "icon": "🏛️",
                "title": "Templo de Zeus Olímpico",
                "description": "17 columnas corintias de 17 metros de altura. El templo más grande de la antigua Grecia. A 5 minutos a pie del Estadio.",
                "tip": "La entrada combinada con la Acrópolis es más económica si no la has usado aún.",
                "links": [
                    {"label": "Templo Zeus en Maps", "url": "https://www.google.com/maps/search/Temple+of+Olympian+Zeus+Athens"}
                ]
            },
            {
                "time": "11:00",
                "icon": "💂",
                "title": "Cambio de Guardia en Syntagma",
                "description": "Los Evzones (guardia presidencial) realizan el cambio cada hora. Sus zapatos pesan 3kg cada uno (400 clavos). El cambio de guardia dominical es el más elaborado.",
                "tip": "No te rías ni hagas ruido. Es una ceremonia solemne aunque el uniforme parezca festivo.",
                "links": [
                    {"label": "Plaza Syntagma", "url": "https://www.google.com/maps/search/Syntagma+Square+Athens"},
                    {"label": "Info Evzones", "url": "https://www.visitgreece.gr/athens/syntagma/"}
                ]
            },
            {
                "time": "Tarde",
                "icon": "✈️",
                "title": "Vuelo de regreso a Madrid",
                "description": "Traslado al aeropuerto. Usa la app Beat (el Uber griego) para un taxi sin sorpresas en el precio. Buen viaje.",
                "tip": "Descárgate Beat antes de ir al aeropuerto. Ahorra tiempo y dinero vs taxis en la calle.",
                "links": [
                    {"label": "Aeropuerto de Atenas", "url": "https://www.aia.gr/"},
                    {"label": "App Beat (taxi)", "url": "https://thebeat.co/"}
                ]
            }
        ]
    }
]

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Atenas & Meteora — Abril 2026</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Josefin+Sans:wght@300;400;600&display=swap" rel="stylesheet">
    <style>
        :root {
            --gold: #C9A84C;
            --cream: #F5F0E8;
            --dark: #1A1614;
            --mid: #2E2926;
            --text: #3A3330;
            --border: rgba(201,168,76,0.25);
        }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        html { scroll-behavior: smooth; }

        body {
            background: var(--dark);
            color: var(--cream);
            font-family: 'Josefin Sans', sans-serif;
            overflow-x: hidden;
        }

        /* ─── HERO ─── */
        .hero {
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            position: relative;
            overflow: hidden;
            padding: 2rem;
        }
        .hero-bg {
            position: absolute; inset: 0;
            background: url('https://images.unsplash.com/photo-1603565816030-6b389eeb23cb?w=1600&q=80') center/cover;
            filter: brightness(0.3) saturate(0.7);
        }
        .hero-overlay {
            position: absolute; inset: 0;
            background: linear-gradient(to bottom, transparent 40%, var(--dark) 100%);
        }
        .hero-content { position: relative; z-index: 1; }
        .hero-label {
            font-family: 'Josefin Sans', sans-serif;
            font-size: 0.75rem;
            letter-spacing: 0.4em;
            color: var(--gold);
            text-transform: uppercase;
            margin-bottom: 1.5rem;
            opacity: 0;
            animation: fadeUp 1s ease 0.2s forwards;
        }
        .hero h1 {
            font-family: 'Cormorant Garamond', serif;
            font-size: clamp(3.5rem, 8vw, 7rem);
            font-weight: 300;
            line-height: 1.05;
            opacity: 0;
            animation: fadeUp 1s ease 0.4s forwards;
        }
        .hero h1 em { font-style: italic; color: var(--gold); }
        .hero-sub {
            font-family: 'Josefin Sans', sans-serif;
            font-size: 0.85rem;
            letter-spacing: 0.3em;
            color: rgba(245,240,232,0.6);
            margin-top: 1.5rem;
            text-transform: uppercase;
            opacity: 0;
            animation: fadeUp 1s ease 0.6s forwards;
        }
        .hero-dates {
            display: flex; gap: 2rem; justify-content: center;
            margin-top: 3rem;
            opacity: 0;
            animation: fadeUp 1s ease 0.8s forwards;
        }
        .hero-date {
            text-align: center;
            padding: 1rem 2rem;
            border: 1px solid var(--border);
            backdrop-filter: blur(10px);
            background: rgba(26,22,20,0.5);
        }
        .hero-date .num {
            font-family: 'Cormorant Garamond', serif;
            font-size: 2.5rem;
            color: var(--gold);
            line-height: 1;
        }
        .hero-date .lbl {
            font-size: 0.65rem;
            letter-spacing: 0.3em;
            text-transform: uppercase;
            color: rgba(245,240,232,0.5);
            margin-top: 0.3rem;
        }
        .scroll-hint {
            position: absolute; bottom: 2rem; left: 50%;
            transform: translateX(-50%);
            font-size: 0.7rem; letter-spacing: 0.3em;
            color: rgba(245,240,232,0.4);
            text-transform: uppercase;
            animation: pulse 2s ease-in-out infinite;
        }
        .scroll-hint::after {
            content: ''; display: block; margin: 0.5rem auto 0;
            width: 1px; height: 40px;
            background: linear-gradient(to bottom, var(--gold), transparent);
        }

        /* ─── NAV ─── */
        nav {
            position: sticky; top: 0; z-index: 100;
            background: rgba(26,22,20,0.95);
            backdrop-filter: blur(20px);
            border-bottom: 1px solid var(--border);
            padding: 0 2rem;
            display: flex; align-items: center; justify-content: space-between;
            height: 64px;
        }
        .nav-logo {
            font-family: 'Cormorant Garamond', serif;
            font-size: 1.2rem;
            color: var(--gold);
            letter-spacing: 0.1em;
        }
        .nav-days {
            display: flex; gap: 0.5rem;
        }
        .nav-day {
            width: 36px; height: 36px;
            border: 1px solid var(--border);
            display: flex; align-items: center; justify-content: center;
            font-size: 0.75rem;
            color: rgba(245,240,232,0.5);
            cursor: pointer;
            transition: all 0.2s;
            text-decoration: none;
        }
        .nav-day:hover { border-color: var(--gold); color: var(--gold); }

        /* ─── DAY SECTIONS ─── */
        .day-section {
            max-width: 1100px;
            margin: 0 auto;
            padding: 5rem 2rem;
        }
        .day-section + .day-section {
            border-top: 1px solid var(--border);
        }

        .day-header {
            display: grid;
            grid-template-columns: auto 1fr;
            gap: 2rem;
            align-items: start;
            margin-bottom: 3rem;
        }
        .day-number {
            font-family: 'Cormorant Garamond', serif;
            font-size: 6rem;
            font-weight: 300;
            line-height: 0.9;
            color: var(--border);
            color: rgba(201,168,76,0.2);
            user-select: none;
        }
        .day-meta {}
        .day-label {
            font-size: 0.7rem;
            letter-spacing: 0.4em;
            text-transform: uppercase;
            color: var(--gold);
            margin-bottom: 0.5rem;
        }
        .day-title {
            font-family: 'Cormorant Garamond', serif;
            font-size: clamp(2rem, 4vw, 3.2rem);
            font-weight: 400;
            line-height: 1.1;
        }
        .day-location {
            font-size: 0.75rem;
            letter-spacing: 0.25em;
            color: rgba(245,240,232,0.45);
            text-transform: uppercase;
            margin-top: 0.75rem;
        }
        .day-location::before { content: '📍 '; }

        /* ─── HERO IMAGE ─── */
        .day-image {
            width: 100%;
            height: 320px;
            object-fit: cover;
            margin-bottom: 3rem;
            filter: brightness(0.85) saturate(0.9);
            transition: filter 0.4s;
        }
        .day-image:hover { filter: brightness(1) saturate(1); }

        /* ─── ACTIVITIES ─── */
        .activities { display: flex; flex-direction: column; gap: 1.5rem; }

        .activity {
            display: grid;
            grid-template-columns: 80px 1fr;
            gap: 0;
            position: relative;
        }
        .activity::before {
            content: '';
            position: absolute;
            left: 40px;
            top: 44px;
            bottom: -1.5rem;
            width: 1px;
            background: var(--border);
        }
        .activity:last-child::before { display: none; }

        .activity-time {
            text-align: center;
            padding-top: 0.75rem;
        }
        .activity-icon {
            font-size: 1.4rem;
            display: block;
            margin-bottom: 0.25rem;
        }
        .activity-clock {
            font-size: 0.65rem;
            letter-spacing: 0.1em;
            color: var(--gold);
            display: block;
        }

        .activity-card {
            background: rgba(255,255,255,0.03);
            border: 1px solid var(--border);
            border-left: 3px solid var(--gold);
            padding: 1.25rem 1.5rem;
            margin-left: 1rem;
            transition: background 0.2s;
        }
        .activity-card:hover { background: rgba(255,255,255,0.06); }

        .activity-title {
            font-family: 'Cormorant Garamond', serif;
            font-size: 1.3rem;
            font-weight: 600;
            margin-bottom: 0.5rem;
        }
        .activity-desc {
            font-size: 0.85rem;
            line-height: 1.7;
            color: rgba(245,240,232,0.7);
            margin-bottom: 0.75rem;
        }
        .activity-tip {
            font-size: 0.78rem;
            color: var(--gold);
            background: rgba(201,168,76,0.08);
            border-left: 2px solid var(--gold);
            padding: 0.5rem 0.75rem;
            margin-bottom: 0.75rem;
            font-style: italic;
        }
        .activity-tip::before { content: '💡 '; font-style: normal; }

        .activity-links { display: flex; flex-wrap: wrap; gap: 0.5rem; }
        .activity-link {
            font-size: 0.7rem;
            letter-spacing: 0.15em;
            text-transform: uppercase;
            color: var(--gold);
            border: 1px solid rgba(201,168,76,0.35);
            padding: 0.3rem 0.75rem;
            text-decoration: none;
            transition: all 0.2s;
        }
        .activity-link:hover {
            background: var(--gold);
            color: var(--dark);
        }

        /* ─── MAP ─── */
        .map-section {
            margin: 3rem 0 1rem;
        }
        .map-toggle {
            display: flex; align-items: center; gap: 0.75rem;
            font-size: 0.75rem; letter-spacing: 0.25em;
            text-transform: uppercase;
            color: rgba(245,240,232,0.5);
            cursor: pointer;
            padding: 0.75rem 0;
            border: none; background: none;
            border-top: 1px solid var(--border);
            width: 100%;
            text-align: left;
            transition: color 0.2s;
        }
        .map-toggle:hover { color: var(--gold); }
        .map-toggle .arrow { transition: transform 0.3s; }
        .map-toggle.open .arrow { transform: rotate(180deg); }
        .map-toggle .arrow::before { content: '▾'; }
        .map-container { overflow: hidden; max-height: 0; transition: max-height 0.5s ease; }
        .map-container.open { max-height: 500px; }
        .map-container iframe {
            width: 100%; height: 380px;
            border: 1px solid var(--border);
            margin-top: 1rem;
            filter: grayscale(0.4) invert(0.9) hue-rotate(180deg);
        }

        /* ─── SUMMARY TABLE ─── */
        .summary {
            max-width: 1100px;
            margin: 0 auto;
            padding: 4rem 2rem;
            border-top: 1px solid var(--border);
        }
        .summary h2 {
            font-family: 'Cormorant Garamond', serif;
            font-size: 2rem;
            font-weight: 300;
            margin-bottom: 2rem;
            color: var(--gold);
        }
        .summary-table {
            width: 100%;
            border-collapse: collapse;
            font-size: 0.82rem;
        }
        .summary-table th {
            font-size: 0.65rem; letter-spacing: 0.3em;
            text-transform: uppercase;
            color: var(--gold);
            padding: 0.75rem 1rem;
            text-align: left;
            border-bottom: 1px solid var(--border);
        }
        .summary-table td {
            padding: 0.85rem 1rem;
            border-bottom: 1px solid rgba(201,168,76,0.1);
            color: rgba(245,240,232,0.8);
        }
        .summary-table tr:hover td { background: rgba(255,255,255,0.03); }
        .day-badge {
            display: inline-block;
            padding: 0.2rem 0.6rem;
            background: rgba(201,168,76,0.15);
            color: var(--gold);
            font-size: 0.7rem;
            letter-spacing: 0.1em;
        }

        /* ─── TIPS ─── */
        .tips-section {
            max-width: 1100px;
            margin: 0 auto;
            padding: 4rem 2rem;
            border-top: 1px solid var(--border);
        }
        .tips-section h2 {
            font-family: 'Cormorant Garamond', serif;
            font-size: 2rem; font-weight: 300;
            color: var(--gold); margin-bottom: 2rem;
        }
        .tips-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
            gap: 1.5rem;
        }
        .tip-card {
            border: 1px solid var(--border);
            padding: 1.5rem;
            background: rgba(255,255,255,0.02);
        }
        .tip-icon { font-size: 2rem; margin-bottom: 0.75rem; }
        .tip-title {
            font-family: 'Cormorant Garamond', serif;
            font-size: 1.2rem; margin-bottom: 0.5rem;
        }
        .tip-text { font-size: 0.82rem; line-height: 1.7; color: rgba(245,240,232,0.65); }

        /* ─── FOOTER ─── */
        footer {
            text-align: center;
            padding: 3rem 2rem;
            border-top: 1px solid var(--border);
            font-size: 0.7rem;
            letter-spacing: 0.2em;
            color: rgba(245,240,232,0.25);
            text-transform: uppercase;
        }

        @keyframes fadeUp {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        @keyframes pulse {
            0%, 100% { opacity: 0.4; }
            50% { opacity: 0.8; }
        }

        @media (max-width: 600px) {
            .hero-dates { flex-direction: column; gap: 1rem; }
            .day-header { grid-template-columns: 1fr; }
            .day-number { font-size: 4rem; }
            .activity { grid-template-columns: 60px 1fr; }
            .nav-days { display: none; }
        }
    </style>
</head>
<body>

<!-- HERO -->
<section class="hero" id="top">
    <div class="hero-bg"></div>
    <div class="hero-overlay"></div>
    <div class="hero-content">
        <p class="hero-label">Viaje · Madrid → Atenas</p>
        <h1>Atenas <em>&</em><br>Meteora</h1>
        <p class="hero-sub">6 días · 6 noches · Semana Santa en Grecia</p>
        <div class="hero-dates">
            <div class="hero-date">
                <div class="num">02</div>
                <div class="lbl">Llegada</div>
            </div>
            <div class="hero-date">
                <div class="num">ABR</div>
                <div class="lbl">2026</div>
            </div>
            <div class="hero-date">
                <div class="num">07</div>
                <div class="lbl">Vuelta</div>
            </div>
        </div>
    </div>
    <div class="scroll-hint">Explorar itinerario</div>
</section>

<!-- NAV -->
<nav>
    <span class="nav-logo">🏛 Atenas 2026</span>
    <div class="nav-days">
        {% for day in days %}
        <a class="nav-day" href="#dia-{{ day.day }}" title="{{ day.date }}">{{ day.day }}</a>
        {% endfor %}
    </div>
</nav>

<!-- DAYS -->
{% for day in days %}
<section class="day-section" id="dia-{{ day.day }}">
    <div class="day-header">
        <div class="day-number">0{{ day.day }}</div>
        <div class="day-meta">
            <div class="day-label">{{ day.date }}</div>
            <h2 class="day-title">{{ day.emoji }} {{ day.title }}</h2>
            <div class="day-location">{{ day.location }}</div>
        </div>
    </div>

    <img class="day-image" src="{{ day.hero_image }}" alt="{{ day.title }}" loading="lazy">

    <div class="activities">
        {% for act in day.activities %}
        <div class="activity">
            <div class="activity-time">
                <span class="activity-icon">{{ act.icon }}</span>
                <span class="activity-clock">{{ act.time }}</span>
            </div>
            <div class="activity-card">
                <div class="activity-title">{{ act.title }}</div>
                <p class="activity-desc">{{ act.description }}</p>
                <div class="activity-tip">{{ act.tip }}</div>
                <div class="activity-links">
                    {% for link in act.links %}
                    <a class="activity-link" href="{{ link.url }}" target="_blank" rel="noopener">
                        {{ link.label }} ↗
                    </a>
                    {% endfor %}
                </div>
            </div>
        </div>
        {% endfor %}
    </div>

    <!-- MAP -->
    <div class="map-section">
        <button class="map-toggle" onclick="toggleMap(this)">
            <span class="arrow"></span>
            Ver mapa de {{ day.location }}
        </button>
        <div class="map-container">
            <iframe
                src="https://maps.google.com/maps?q={{ day.map_query | urlencode }}&output=embed&z=14"
                loading="lazy"
                referrerpolicy="no-referrer-when-downgrade"
                title="Mapa {{ day.location }}"
                allowfullscreen>
            </iframe>
        </div>
    </div>
</section>
{% endfor %}

<!-- SUMMARY TABLE -->
<section class="summary">
    <h2>Resumen del Itinerario</h2>
    <table class="summary-table">
        <thead>
            <tr>
                <th>Día</th>
                <th>Fecha</th>
                <th>Ubicación</th>
                <th>Actividad clave</th>
            </tr>
        </thead>
        <tbody>
            {% for day in days %}
            <tr>
                <td><span class="day-badge">Día {{ day.day }}</span></td>
                <td>{{ day.date }}</td>
                <td>{{ day.location }}</td>
                <td>{{ day.activities[0].title }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</section>

<!-- TIPS -->
<section class="tips-section">
    <h2>Consejos Esenciales</h2>
    <div class="tips-grid">
        <div class="tip-card">
            <div class="tip-icon">👟</div>
            <div class="tip-title">Calzado</div>
            <p class="tip-text">El mármol de la Acrópolis y Delfos es pulido y resbala. Lleva zapatillas con buen agarre. Nunca tacones.</p>
        </div>
        <div class="tip-card">
            <div class="tip-icon">📱</div>
            <div class="tip-title">App Beat (Taxi)</div>
            <p class="tip-text">Es el Uber griego. Descárgala antes de ir. Evita las tarifas infladas de los taxis en la calle, especialmente al aeropuerto.</p>
        </div>
        <div class="tip-card">
            <div class="tip-icon">🚗</div>
            <div class="tip-title">Transporte a Meteora</div>
            <p class="tip-text">El tren Atenas–Kalambaka en 1ª clase es una alternativa cómoda al coche. Hay tours privados que incluyen traslado y guía.</p>
        </div>
        <div class="tip-card">
            <div class="tip-icon">🏛️</div>
            <div class="tip-title">Entradas Anticipadas</div>
            <p class="tip-text">Compra siempre online en etickets.tap.gr. La Acrópolis puede tener colas de 1 hora en temporada. Entra a la apertura.</p>
        </div>
        <div class="tip-card">
            <div class="tip-icon">🧥</div>
            <div class="tip-title">Código de vestimenta</div>
            <p class="tip-text">En los monasterios de Meteora: rodillas y hombros cubiertos. Ofrecen pañuelos en la entrada si lo necesitas.</p>
        </div>
        <div class="tip-card">
            <div class="tip-icon">☕</div>
            <div class="tip-title">Freddo Espresso</div>
            <p class="tip-text">El café nacional moderno de Grecia. Café espresso batido con hielo. Pídelo "skéto" (sin azúcar) o "glikó" (dulce). Obligatorio.</p>
        </div>
    </div>
</section>

<footer>
    Viaje de Madrid a Atenas · Semana Santa 2026 · 2–7 Abril
    <br><br>
    App creada por <strong style="color: var(--gold); letter-spacing: 0.15em;">JC Tejedor</strong> con <strong style="color: var(--gold); letter-spacing: 0.15em;">Claude</strong>
</footer>

<script>
    function toggleMap(btn) {
        btn.classList.toggle('open');
        const container = btn.nextElementSibling;
        container.classList.toggle('open');
    }

    // Intersection observer para animaciones suaves
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(e => {
            if (e.isIntersecting) {
                e.target.style.opacity = '1';
                e.target.style.transform = 'translateY(0)';
            }
        });
    }, { threshold: 0.08 });

    document.querySelectorAll('.activity-card, .tip-card').forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(16px)';
        el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
        observer.observe(el);
    });
</script>

</body>
</html>"""

@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE, days=ITINERARY)

if __name__ == "__main__":
    app.run(debug=True)

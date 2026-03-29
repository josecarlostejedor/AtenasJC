from flask import Flask, render_template_string

app = Flask(__name__)

ITINERARY = [
    {
        "day": 1,
        "date": "Jueves 2 de abril",
        "title": "Aterrizaje en la Historia",
        "emoji": "✈️",
        "location": "Atenas",
        "hero_image": "https://images.unsplash.com/photo-1603565816030-6b389eeb23cb?w=1200&q=80",
        "map_lat": "37.9707",
        "map_lng": "23.7239",
        "map_gmaps": "https://www.google.com/maps/place/Dionysiou+Areopagitou,+Athens,+Greece/@37.9707,23.7239,16z",
        "activities": [
            {
                "time": "Tarde",
                "icon": "🛬",
                "title": "Llegada al Aeropuerto de Atenas",
                "description": "Traslado al hotel en el barrio de Koukaki, al sur de la Acrópolis. Más auténtico y tranquilo que el centro puro.",
                "tip": "Koukaki es ideal: mezcla perfecta de autenticidad y comodidad.",
                "links": [
                    {"label": "Aeropuerto de Atenas", "url": "https://www.aia.gr/"},
                    {"label": "Koukaki en Maps", "url": "https://www.google.com/maps/search/Koukaki+Athens+Greece"}
                ]
            },
            {
                "time": "Atardecer",
                "icon": "🚶",
                "title": "Paseo por Dionysiou Areopagitou",
                "description": "La calle peatonal más bonita de Atenas rodea la falda de la Acrópolis. El Partenón se ilumina al caer la noche.",
                "tip": "Llega sobre las 19:30 para ver el atardecer dorado sobre el mármol.",
                "links": [
                    {"label": "Ver en Google Maps", "url": "https://www.google.com/maps/place/Dionysiou+Areopagitou,+Athens,+Greece"},
                    {"label": "Guía oficial Atenas", "url": "https://www.visitgreece.gr/athens/"}
                ]
            },
            {
                "time": "Noche",
                "icon": "🍽️",
                "title": "Cena en el barrio de Psirí",
                "description": "Ambiente animado con tabernas tradicionales. Taberna Lithos para comida excelente o Little Kook para una experiencia de café única.",
                "tip": "Little Kook cambia su decoración cada temporada. ¡Una experiencia única!",
                "links": [
                    {"label": "Psirí en Maps", "url": "https://www.google.com/maps/search/Psiri+Athens+restaurants"},
                    {"label": "Little Kook Athens", "url": "https://www.google.com/maps/search/Little+Kook+Athens+Greece"}
                ]
            }
        ]
    },
    {
        "day": 2,
        "date": "Viernes 3 de abril",
        "title": "El Oráculo de Delfos",
        "emoji": "🏛️",
        "location": "Delfos · Arachova · Atenas",
        "hero_image": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&q=80",
        "map_lat": "38.4824",
        "map_lng": "22.5011",
        "map_gmaps": "https://www.google.com/maps/place/Archaeological+Site+of+Delphi,+Greece/@38.4824,22.5011,15z",
        "activities": [
            {
                "time": "08:00",
                "icon": "🚗",
                "title": "Salida hacia Delfos",
                "description": "Recoge el coche de alquiler y pon rumbo a Delfos (2.5h). La carretera por el Parnaso es espectacular.",
                "tip": "Alquila el coche la tarde anterior para salir sin perder tiempo.",
                "links": [
                    {"label": "Ruta Athens → Delphi", "url": "https://www.google.com/maps/dir/Athens,+Greece/Delphi,+Greece"},
                    {"label": "Alquiler de coches", "url": "https://www.discovercars.com/greece/athens"}
                ]
            },
            {
                "time": "10:30",
                "icon": "🏛️",
                "title": "Santuario de Apolo en Delfos",
                "description": "El centro del mundo antiguo. Visita el Teatro, el Estadio y baja al Tholos de Atenea Pronaia. En el Museo, el Auriga de Bronce es impresionante.",
                "tip": "Compra la entrada combinada (yacimiento + museo). El museo es imprescindible.",
                "links": [
                    {"label": "Entradas oficiales", "url": "https://etickets.tap.gr/"},
                    {"label": "Delfos en Maps", "url": "https://www.google.com/maps/place/Archaeological+Site+of+Delphi,+Greece"}
                ]
            },
            {
                "time": "14:00",
                "icon": "🧀",
                "title": "Almuerzo en Arachova",
                "description": "El pueblo de montaña más bonito de Grecia central. Prueba el queso Formaela a la plancha y el vino local.",
                "tip": "Formaela es una IGP griega exclusiva de esta zona. No te lo pierdas.",
                "links": [
                    {"label": "Arachova en Maps", "url": "https://www.google.com/maps/place/Arachova,+Greece"}
                ]
            },
            {
                "time": "21:00",
                "icon": "🕯️",
                "title": "Procesión del Epitafios — Viernes Santo Ortodoxo",
                "description": "Ve a la Catedral Metropolitana (Mitropoli) para ver la procesión. Miles de velas amarillas en silencio. Uno de los momentos más emocionantes del año.",
                "tip": "Llega antes de las 20:30 para encontrar sitio. Llevan velas en la entrada.",
                "links": [
                    {"label": "Catedral Mitropoli", "url": "https://www.google.com/maps/place/Metropolitan+Cathedral+of+Athens,+Greece"}
                ]
            }
        ]
    },
    {
        "day": 3,
        "date": "Sábado 4 de abril",
        "title": "Tesoros y Vida Bohemia",
        "emoji": "🏺",
        "location": "Atenas",
        "hero_image": "https://images.unsplash.com/photo-1555993539-1732b0258235?w=1200&q=80",
        "map_lat": "37.9836",
        "map_lng": "23.7312",
        "map_gmaps": "https://www.google.com/maps/place/National+Archaeological+Museum,+Athens,+Greece/@37.9836,23.7312,17z",
        "activities": [
            {
                "time": "09:00",
                "icon": "🏺",
                "title": "Museo Arqueológico Nacional",
                "description": "La 'caja fuerte' de Grecia. Busca el Mecanismo de Anticitera (primer ordenador de la historia, 100 a.C.) y la Máscara de Agamenón en oro macizo.",
                "tip": "Llega justo a la apertura. Reserva al menos 2.5 horas para verlo bien.",
                "links": [
                    {"label": "Web oficial del Museo", "url": "https://www.namuseum.gr/"},
                    {"label": "Ver en Maps", "url": "https://www.google.com/maps/place/National+Archaeological+Museum,+Athens,+Greece"},
                    {"label": "Reservar entradas", "url": "https://etickets.tap.gr/"}
                ]
            },
            {
                "time": "12:30",
                "icon": "✊",
                "title": "Barrio de Exarchia",
                "description": "El corazón intelectual y rebelde de Atenas. Grafitis de museo, librerías de segunda mano y la mejor música alternativa.",
                "tip": "Es un barrio progresista y seguro. Perfecto para tomar café y observar la vida local.",
                "links": [
                    {"label": "Exarchia en Maps", "url": "https://www.google.com/maps/place/Exarcheia,+Athens,+Greece"}
                ]
            },
            {
                "time": "18:00",
                "icon": "🌅",
                "title": "Atardecer en el Monte Licabeto",
                "description": "El punto más alto de Atenas. Vista de 360° sobre toda la cuenca del Ática. El teleférico te sube en minutos.",
                "tip": "La subida a pie son 20 minutos amenos. El teleférico es ideal para la bajada.",
                "links": [
                    {"label": "Monte Licabeto en Maps", "url": "https://www.google.com/maps/place/Lycabettus+Hill,+Athens,+Greece"},
                    {"label": "Info teleférico", "url": "https://www.lycabettushill.com/"}
                ]
            },
            {
                "time": "00:00",
                "icon": "✨",
                "title": "Misa de Resurrección — Christos Anesti",
                "description": "El momento más alegre del año en Grecia. A medianoche todos encienden su vela y se saludan '¡Christos Anesti!'. Fuegos artificiales y emoción.",
                "tip": "La iglesia de Agios Georgios en la cima del Licabeto tiene la misa más espectacular.",
                "links": [
                    {"label": "Iglesias de Plaka", "url": "https://www.google.com/maps/search/church+Plaka+Athens+Greece"}
                ]
            }
        ]
    },
    {
        "day": 4,
        "date": "Domingo 5 de abril",
        "title": "El Milagro de Meteora",
        "emoji": "⛰️",
        "location": "Meteora · Kastraki",
        "hero_image": "https://images.unsplash.com/photo-1534430480872-3498386e7856?w=1200&q=80",
        "map_lat": "39.7217",
        "map_lng": "21.6306",
        "map_gmaps": "https://www.google.com/maps/place/Meteora,+Kalambaka,+Greece/@39.7217,21.6306,14z",
        "activities": [
            {
                "time": "06:00",
                "icon": "🚗",
                "title": "Salida madrugadora hacia Meteora",
                "description": "Son ~4 horas de camino. Sal muy temprano para aprovechar el día. Alternativa: tren o tour privado con minibús.",
                "tip": "El tren Atenas-Kalambaka es una opción relajante y pintoresca (~4.5h).",
                "links": [
                    {"label": "Ruta Athens → Meteora", "url": "https://www.google.com/maps/dir/Athens,+Greece/Meteora,+Kalambaka,+Greece"},
                    {"label": "Trenes Hellenic Train", "url": "https://www.hellenictrain.gr/"}
                ]
            },
            {
                "time": "10:30",
                "icon": "⛪",
                "title": "Gran Meteoro — Monasterio de la Transfiguración",
                "description": "El más grande e importante de los monasterios. Fundado en el siglo XIV. Las vistas desde arriba quitan el aliento.",
                "tip": "Dress code obligatorio: rodillas y hombros cubiertos. Hay pañuelos en la entrada.",
                "links": [
                    {"label": "Horarios monasterios", "url": "https://www.meteora.gr/"},
                    {"label": "Gran Meteoro en Maps", "url": "https://www.google.com/maps/place/Great+Meteoron+Monastery,+Greece"}
                ]
            },
            {
                "time": "12:00",
                "icon": "🌸",
                "title": "Monasterio de Roussanou",
                "description": "Regentado por monjas. El más fotogénico por su posición y sus jardines en flor. Las vistas desde su terraza son las más dramáticas de Meteora.",
                "tip": "El acceso es por un puente de madera sobre el vacío. Impresionante.",
                "links": [
                    {"label": "Roussanou en Maps", "url": "https://www.google.com/maps/place/Monastery+of+Roussanou,+Meteora,+Greece"}
                ]
            },
            {
                "time": "14:30",
                "icon": "🍖",
                "title": "Comida de Pascua en Kastraki",
                "description": "El gran día del cordero al espiedo. Come en una taberna del pueblo de Kastraki. Verás a familias griegas celebrando en la calle.",
                "tip": "Reserva la noche anterior. Es Pascua y las tabernas se llenan de locales.",
                "links": [
                    {"label": "Restaurantes en Kastraki", "url": "https://www.google.com/maps/search/restaurant+Kastraki+Meteora+Greece"},
                    {"label": "Kastraki en Maps", "url": "https://www.google.com/maps/place/Kastraki,+Kalambaka,+Greece"}
                ]
            }
        ]
    },
    {
        "day": 5,
        "date": "Lunes 6 de abril",
        "title": "El Corazón de la Civilización",
        "emoji": "🏛️",
        "location": "Atenas — Acrópolis",
        "hero_image": "https://images.unsplash.com/photo-1603565816030-6b389eeb23cb?w=1200&q=80",
        "map_lat": "37.9715",
        "map_lng": "23.7257",
        "map_gmaps": "https://www.google.com/maps/place/Acropolis+of+Athens,+Greece/@37.9715,23.7257,17z",
        "activities": [
            {
                "time": "08:00",
                "icon": "🏛️",
                "title": "Acrópolis — En la apertura",
                "description": "Entra puntual a las 8:00. Sube por la entrada del Teatro de Dioniso. No te quedes solo con el Partenón: busca el Erecteion y sus Cariátides.",
                "tip": "Las primeras 2 horas son las mejores: luz dorada, pocos turistas y silencio.",
                "links": [
                    {"label": "Entradas Acrópolis", "url": "https://etickets.tap.gr/"},
                    {"label": "Acrópolis en Maps", "url": "https://www.google.com/maps/place/Acropolis+of+Athens,+Greece"}
                ]
            },
            {
                "time": "10:30",
                "icon": "🏺",
                "title": "Museo de la Acrópolis",
                "description": "Las Cariátides originales están aquí. El suelo de cristal deja ver las excavaciones. Almuerza en la cafetería con vistas directas al Partenón.",
                "tip": "El suelo de cristal deja ver las excavaciones arqueológicas originales bajo tus pies.",
                "links": [
                    {"label": "Museo de la Acrópolis", "url": "https://www.theacropolismuseum.gr/"},
                    {"label": "Ver en Maps", "url": "https://www.google.com/maps/place/Acropolis+Museum,+Athens,+Greece"}
                ]
            },
            {
                "time": "15:00",
                "icon": "🏘️",
                "title": "Anafiótika — El barrio-isla",
                "description": "Un rincón secreto en la ladera de la Acrópolis que parece una isla de las Cícladas. Casitas blancas, gatos y silencio total.",
                "tip": "Muy pocas personas saben de este barrio. El contraste perfecto con el caos de Plaka.",
                "links": [
                    {"label": "Anafiótika en Maps", "url": "https://www.google.com/maps/place/Anafiotika,+Athens,+Greece"}
                ]
            },
            {
                "time": "17:00",
                "icon": "🛍️",
                "title": "Mercado de Monastiraki y Freddo Espresso",
                "description": "El mercado de pulgas más famoso de Atenas. Antigüedades, especias y recuerdos. Pide un 'Freddo Espresso': el café nacional moderno de los griegos.",
                "tip": "El Freddo se pide 'skéto' (sin azúcar) o 'glikó' (dulce). Distinto al frappé clásico.",
                "links": [
                    {"label": "Monastiraki en Maps", "url": "https://www.google.com/maps/place/Monastiraki+Square,+Athens,+Greece"}
                ]
            }
        ]
    },
    {
        "day": 6,
        "date": "Martes 7 de abril",
        "title": "Despedida con Honor",
        "emoji": "👋",
        "location": "Atenas → Madrid",
        "hero_image": "https://images.unsplash.com/photo-1555993539-1732b0258235?w=1200&q=80",
        "map_lat": "37.9682",
        "map_lng": "23.7412",
        "map_gmaps": "https://www.google.com/maps/place/Panathenaic+Stadium,+Athens,+Greece/@37.9682,23.7412,17z",
        "activities": [
            {
                "time": "09:00",
                "icon": "🏟️",
                "title": "Estadio Panatenaico",
                "description": "El único estadio del mundo construido íntegramente en mármol blanco. Aquí nacieron los Juegos Olímpicos modernos en 1896. Puedes correr hasta la meta.",
                "tip": "La entrada incluye audioguía por solo 5€. Merece mucho la pena.",
                "links": [
                    {"label": "Web oficial", "url": "https://www.panathenaicstadium.gr/"},
                    {"label": "Estadio en Maps", "url": "https://www.google.com/maps/place/Panathenaic+Stadium,+Athens,+Greece"}
                ]
            },
            {
                "time": "10:00",
                "icon": "🏛️",
                "title": "Templo de Zeus Olímpico",
                "description": "17 columnas corintias de 17 metros de altura. El templo más grande de la antigua Grecia. A 5 minutos a pie del Estadio.",
                "tip": "La entrada combinada con la Acrópolis es más económica si no la has usado aún.",
                "links": [
                    {"label": "Templo Zeus en Maps", "url": "https://www.google.com/maps/place/Temple+of+Olympian+Zeus,+Athens,+Greece"}
                ]
            },
            {
                "time": "11:00",
                "icon": "💂",
                "title": "Cambio de Guardia en Syntagma",
                "description": "Los Evzones realizan el cambio cada hora. Sus zapatos pesan 3kg cada uno (400 clavos). El cambio dominical es el más elaborado.",
                "tip": "No hagas ruido. Es una ceremonia solemne aunque el uniforme parezca festivo.",
                "links": [
                    {"label": "Plaza Syntagma en Maps", "url": "https://www.google.com/maps/place/Syntagma+Square,+Athens,+Greece"},
                    {"label": "Info Evzones", "url": "https://www.visitgreece.gr/athens/syntagma/"}
                ]
            },
            {
                "time": "Tarde",
                "icon": "✈️",
                "title": "Vuelo de regreso a Madrid",
                "description": "Traslado al aeropuerto. Usa la app Beat (el Uber griego) para un taxi sin sorpresas en el precio.",
                "tip": "Descárgate Beat antes de salir. Ahorra tiempo y dinero frente a taxis en la calle.",
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
    <title>Atenas &amp; Meteora — Abril 2026</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Josefin+Sans:wght@300;400;600&display=swap" rel="stylesheet">
    <style>
        :root {
            --gold: #C9A84C;
            --cream: #F5F0E8;
            --dark: #1A1614;
            --border: rgba(201,168,76,0.25);
        }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        html { scroll-behavior: smooth; }
        body { background: var(--dark); color: var(--cream); font-family: 'Josefin Sans', sans-serif; overflow-x: hidden; }

        .hero {
            min-height: 100vh; display: flex; flex-direction: column;
            align-items: center; justify-content: center;
            text-align: center; position: relative; overflow: hidden; padding: 2rem;
        }
        .hero-bg {
            position: absolute; inset: 0;
            background: url('https://images.unsplash.com/photo-1603565816030-6b389eeb23cb?w=1600&q=80') center/cover;
            filter: brightness(0.3) saturate(0.7);
        }
        .hero-overlay { position: absolute; inset: 0; background: linear-gradient(to bottom, transparent 40%, var(--dark) 100%); }
        .hero-content { position: relative; z-index: 1; }
        .hero-label { font-size: .75rem; letter-spacing: .4em; color: var(--gold); text-transform: uppercase; margin-bottom: 1.5rem; opacity: 0; animation: fadeUp 1s ease .2s forwards; }
        .hero h1 { font-family: 'Cormorant Garamond', serif; font-size: clamp(3.5rem,8vw,7rem); font-weight: 300; line-height: 1.05; opacity: 0; animation: fadeUp 1s ease .4s forwards; }
        .hero h1 em { font-style: italic; color: var(--gold); }
        .hero-sub { font-size: .85rem; letter-spacing: .3em; color: rgba(245,240,232,.6); margin-top: 1.5rem; text-transform: uppercase; opacity: 0; animation: fadeUp 1s ease .6s forwards; }
        .hero-dates { display: flex; gap: 2rem; justify-content: center; margin-top: 3rem; opacity: 0; animation: fadeUp 1s ease .8s forwards; }
        .hero-date { text-align: center; padding: 1rem 2rem; border: 1px solid var(--border); backdrop-filter: blur(10px); background: rgba(26,22,20,.5); }
        .hero-date .num { font-family: 'Cormorant Garamond', serif; font-size: 2.5rem; color: var(--gold); line-height: 1; }
        .hero-date .lbl { font-size: .65rem; letter-spacing: .3em; text-transform: uppercase; color: rgba(245,240,232,.5); margin-top: .3rem; }
        .scroll-hint { position: absolute; bottom: 2rem; left: 50%; transform: translateX(-50%); font-size: .7rem; letter-spacing: .3em; color: rgba(245,240,232,.4); text-transform: uppercase; animation: pulse 2s ease-in-out infinite; }
        .scroll-hint::after { content: ''; display: block; margin: .5rem auto 0; width: 1px; height: 40px; background: linear-gradient(to bottom, var(--gold), transparent); }

        nav { position: sticky; top: 0; z-index: 100; background: rgba(26,22,20,.96); backdrop-filter: blur(20px); border-bottom: 1px solid var(--border); padding: 0 2rem; display: flex; align-items: center; justify-content: space-between; height: 64px; }
        .nav-logo { font-family: 'Cormorant Garamond', serif; font-size: 1.2rem; color: var(--gold); letter-spacing: .1em; }
        .nav-days { display: flex; gap: .5rem; }
        .nav-day { width: 36px; height: 36px; border: 1px solid var(--border); display: flex; align-items: center; justify-content: center; font-size: .75rem; color: rgba(245,240,232,.5); cursor: pointer; transition: all .2s; text-decoration: none; }
        .nav-day:hover { border-color: var(--gold); color: var(--gold); }

        .day-section { max-width: 1100px; margin: 0 auto; padding: 5rem 2rem; }
        .day-section + .day-section { border-top: 1px solid var(--border); }
        .day-header { display: grid; grid-template-columns: auto 1fr; gap: 2rem; align-items: start; margin-bottom: 3rem; }
        .day-number { font-family: 'Cormorant Garamond', serif; font-size: 6rem; font-weight: 300; line-height: .9; color: rgba(201,168,76,.15); user-select: none; }
        .day-label { font-size: .7rem; letter-spacing: .4em; text-transform: uppercase; color: var(--gold); margin-bottom: .5rem; }
        .day-title { font-family: 'Cormorant Garamond', serif; font-size: clamp(2rem,4vw,3.2rem); font-weight: 400; line-height: 1.1; }
        .day-location { font-size: .75rem; letter-spacing: .25em; color: rgba(245,240,232,.45); text-transform: uppercase; margin-top: .75rem; }
        .day-location::before { content: '📍 '; }
        .day-image { width: 100%; height: 320px; object-fit: cover; margin-bottom: 3rem; filter: brightness(.85) saturate(.9); transition: filter .4s; }
        .day-image:hover { filter: brightness(1) saturate(1); }

        .activities { display: flex; flex-direction: column; gap: 1.5rem; }
        .activity { display: grid; grid-template-columns: 80px 1fr; position: relative; }
        .activity::before { content: ''; position: absolute; left: 40px; top: 44px; bottom: -1.5rem; width: 1px; background: var(--border); }
        .activity:last-child::before { display: none; }
        .activity-time { text-align: center; padding-top: .75rem; }
        .activity-icon { font-size: 1.4rem; display: block; margin-bottom: .25rem; }
        .activity-clock { font-size: .65rem; letter-spacing: .1em; color: var(--gold); display: block; }
        .activity-card { background: rgba(255,255,255,.03); border: 1px solid var(--border); border-left: 3px solid var(--gold); padding: 1.25rem 1.5rem; margin-left: 1rem; transition: background .2s; }
        .activity-card:hover { background: rgba(255,255,255,.06); }
        .activity-title { font-family: 'Cormorant Garamond', serif; font-size: 1.3rem; font-weight: 600; margin-bottom: .5rem; }
        .activity-desc { font-size: .85rem; line-height: 1.7; color: rgba(245,240,232,.7); margin-bottom: .75rem; }
        .activity-tip { font-size: .78rem; color: var(--gold); background: rgba(201,168,76,.08); border-left: 2px solid var(--gold); padding: .5rem .75rem; margin-bottom: .75rem; font-style: italic; }
        .activity-tip::before { content: '💡 '; font-style: normal; }
        .activity-links { display: flex; flex-wrap: wrap; gap: .5rem; }
        .activity-link { font-size: .7rem; letter-spacing: .15em; text-transform: uppercase; color: var(--gold); border: 1px solid rgba(201,168,76,.35); padding: .3rem .75rem; text-decoration: none; transition: all .2s; }
        .activity-link:hover { background: var(--gold); color: var(--dark); }

        /* MAP */
        .map-section { margin: 3rem 0 1rem; }
        .map-toggle { display: flex; align-items: center; gap: .75rem; font-size: .75rem; letter-spacing: .25em; text-transform: uppercase; color: rgba(245,240,232,.5); cursor: pointer; padding: .75rem 0; border: none; background: none; border-top: 1px solid var(--border); width: 100%; text-align: left; transition: color .2s; font-family: 'Josefin Sans', sans-serif; }
        .map-toggle:hover { color: var(--gold); }
        .map-arrow { font-size: 1rem; transition: transform .3s; display: inline-block; }
        .map-toggle.open .map-arrow { transform: rotate(180deg); }
        .map-container { overflow: hidden; max-height: 0; transition: max-height .5s ease; }
        .map-container.open { max-height: 520px; }
        .map-frame { width: 100%; height: 420px; border: 1px solid var(--border); margin-top: 1rem; display: block; }
        .map-open-link { display: inline-block; margin-top: .75rem; font-size: .7rem; letter-spacing: .2em; text-transform: uppercase; color: var(--gold); text-decoration: none; border-bottom: 1px solid rgba(201,168,76,.4); padding-bottom: 2px; transition: border-color .2s; }
        .map-open-link:hover { border-color: var(--gold); }

        .summary { max-width: 1100px; margin: 0 auto; padding: 4rem 2rem; border-top: 1px solid var(--border); }
        .summary h2 { font-family: 'Cormorant Garamond', serif; font-size: 2rem; font-weight: 300; margin-bottom: 2rem; color: var(--gold); }
        .summary-table { width: 100%; border-collapse: collapse; font-size: .82rem; }
        .summary-table th { font-size: .65rem; letter-spacing: .3em; text-transform: uppercase; color: var(--gold); padding: .75rem 1rem; text-align: left; border-bottom: 1px solid var(--border); }
        .summary-table td { padding: .85rem 1rem; border-bottom: 1px solid rgba(201,168,76,.1); color: rgba(245,240,232,.8); }
        .summary-table tr:hover td { background: rgba(255,255,255,.03); }
        .day-badge { display: inline-block; padding: .2rem .6rem; background: rgba(201,168,76,.15); color: var(--gold); font-size: .7rem; letter-spacing: .1em; }

        .tips-section { max-width: 1100px; margin: 0 auto; padding: 4rem 2rem; border-top: 1px solid var(--border); }
        .tips-section h2 { font-family: 'Cormorant Garamond', serif; font-size: 2rem; font-weight: 300; color: var(--gold); margin-bottom: 2rem; }
        .tips-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1.5rem; }
        .tip-card { border: 1px solid var(--border); padding: 1.5rem; background: rgba(255,255,255,.02); }
        .tip-icon { font-size: 2rem; margin-bottom: .75rem; }
        .tip-title { font-family: 'Cormorant Garamond', serif; font-size: 1.2rem; margin-bottom: .5rem; }
        .tip-text { font-size: .82rem; line-height: 1.7; color: rgba(245,240,232,.65); }

        footer { text-align: center; padding: 3rem 2rem; border-top: 1px solid var(--border); font-size: .7rem; letter-spacing: .2em; color: rgba(245,240,232,.25); text-transform: uppercase; line-height: 2; }

        @keyframes fadeUp { from { opacity:0; transform:translateY(20px); } to { opacity:1; transform:translateY(0); } }
        @keyframes pulse { 0%,100% { opacity:.4; } 50% { opacity:.8; } }

        @media (max-width:600px) {
            .hero-dates { flex-direction:column; gap:1rem; }
            .day-header { grid-template-columns:1fr; }
            .day-number { font-size:4rem; }
            .activity { grid-template-columns:60px 1fr; }
            .nav-days { display:none; }
        }
    </style>
</head>
<body>

<section class="hero" id="top">
    <div class="hero-bg"></div>
    <div class="hero-overlay"></div>
    <div class="hero-content">
        <p class="hero-label">Viaje · Madrid → Atenas</p>
        <h1>Atenas <em>&</em><br>Meteora</h1>
        <p class="hero-sub">6 días · 6 noches · Semana Santa en Grecia</p>
        <div class="hero-dates">
            <div class="hero-date"><div class="num">02</div><div class="lbl">Llegada</div></div>
            <div class="hero-date"><div class="num">ABR</div><div class="lbl">2026</div></div>
            <div class="hero-date"><div class="num">07</div><div class="lbl">Vuelta</div></div>
        </div>
    </div>
    <div class="scroll-hint">Explorar itinerario</div>
</section>

<nav>
    <span class="nav-logo">🏛 Atenas 2026</span>
    <div class="nav-days">
        {% for day in days %}
        <a class="nav-day" href="#dia-{{ day.day }}" title="{{ day.date }}">{{ day.day }}</a>
        {% endfor %}
    </div>
</nav>

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
                    <a class="activity-link" href="{{ link.url }}" target="_blank" rel="noopener">{{ link.label }} ↗</a>
                    {% endfor %}
                </div>
            </div>
        </div>
        {% endfor %}
    </div>

    <div class="map-section">
        <button class="map-toggle" onclick="toggleMap(this)">
            <span class="map-arrow">▾</span>&nbsp; Ver mapa — {{ day.location }}
        </button>
        <div class="map-container">
            <iframe
                class="map-frame"
                loading="lazy"
                allowfullscreen
                referrerpolicy="no-referrer-when-downgrade"
                src="https://maps.google.com/maps?q={{ day.map_lat }},{{ day.map_lng }}&z=14&output=embed&hl=es"
                title="Mapa {{ day.location }}">
            </iframe>
            <a class="map-open-link"
               href="{{ day.map_gmaps }}"
               target="_blank" rel="noopener">
                ↗ Abrir en Google Maps
            </a>
        </div>
    </div>
</section>
{% endfor %}

<section class="summary">
    <h2>Resumen del Itinerario</h2>
    <table class="summary-table">
        <thead>
            <tr><th>Día</th><th>Fecha</th><th>Ubicación</th><th>Actividad clave</th></tr>
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

<section class="tips-section">
    <h2>Consejos Esenciales</h2>
    <div class="tips-grid">
        <div class="tip-card"><div class="tip-icon">👟</div><div class="tip-title">Calzado</div><p class="tip-text">El mármol de la Acrópolis y Delfos es pulido y resbala. Lleva zapatillas con buen agarre. Nunca tacones.</p></div>
        <div class="tip-card"><div class="tip-icon">📱</div><div class="tip-title">App Beat (Taxi)</div><p class="tip-text">Es el Uber griego. Descárgala antes de ir. Evita tarifas infladas al aeropuerto y en zonas turísticas.</p></div>
        <div class="tip-card"><div class="tip-icon">🚗</div><div class="tip-title">Transporte a Meteora</div><p class="tip-text">El tren Atenas–Kalambaka en 1ª clase es cómodo y pintoresco. Hay tours privados con guía incluido.</p></div>
        <div class="tip-card"><div class="tip-icon">🏛️</div><div class="tip-title">Entradas Anticipadas</div><p class="tip-text">Compra siempre online en etickets.tap.gr. La Acrópolis puede tener colas de 1 hora. Entra en la apertura.</p></div>
        <div class="tip-card"><div class="tip-icon">🧥</div><div class="tip-title">Código de Vestimenta</div><p class="tip-text">En los monasterios de Meteora: rodillas y hombros cubiertos. Ofrecen pañuelos en la entrada.</p></div>
        <div class="tip-card"><div class="tip-icon">☕</div><div class="tip-title">Freddo Espresso</div><p class="tip-text">El café nacional moderno de Grecia. Espresso batido con hielo. Pídelo 'skéto' (sin azúcar) o 'glikó' (dulce).</p></div>
    </div>
</section>

<footer>
    Viaje de Madrid a Atenas &middot; Semana Santa 2026 &middot; 2&ndash;7 Abril
    <br>
    App creada por <strong style="color:var(--gold);letter-spacing:.15em;">JC Tejedor</strong>
    con <strong style="color:var(--gold);letter-spacing:.15em;">Claude</strong>
</footer>

<script>
    function toggleMap(btn) {
        btn.classList.toggle('open');
        btn.nextElementSibling.classList.toggle('open');
    }

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

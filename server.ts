import express from "express";
import path from "path";
import { createServer as createViteServer } from "vite";

async function startServer() {
  const app = express();
  const PORT = 3000;

  // Itinerary Data (from the original Flask app)
  const ITINERARY = [
    {
        "day": 1,
        "date": "Jueves 2 de abril",
        "title": "Aterrizaje en la Historia",
        "emoji": "✈️",
        "location": "Atenas",
        "hero_image": "https://github.com/josecarlostejedor/AtenasJC/blob/main/aterrizaje.jpg?raw=true",
        "map_lat": "37.9707",
        "map_lng": "23.7239",
        "map_gmaps": "https://www.google.com/maps/place/Dionysiou+Areopagitou,+Athens,+Greece/@37.9707,23.7239,16z",
        "activities": [
            {
                "time": "Tarde",
                "icon": "PlaneLanding",
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
                "icon": "Walk",
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
                "icon": "Utensils",
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
        "hero_image": "https://github.com/josecarlostejedor/AtenasJC/blob/main/oraculodelfos.jpg?raw=true",
        "map_lat": "38.4824",
        "map_lng": "22.5011",
        "map_gmaps": "https://www.google.com/maps/place/Archaeological+Site+of+Delphi,+Greece/@38.4824,22.5011,15z",
        "activities": [
            {
                "time": "08:00",
                "icon": "Car",
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
                "icon": "Landmark",
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
                "icon": "UtensilsCrossed",
                "title": "Almuerzo en Arachova",
                "description": "El pueblo de montaña más bonito de Grecia central. Prueba el queso Formaela a la plancha y el vino local.",
                "tip": "Formaela es una IGP griega exclusiva de esta zona. No te lo pierdas.",
                "links": [
                    {"label": "Arachova en Maps", "url": "https://www.google.com/maps/place/Arachova,+Greece"}
                ]
            },
            {
                "time": "21:00",
                "icon": "Flame",
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
        "hero_image": "https://github.com/josecarlostejedor/AtenasJC/blob/main/tesoroyvidabohemia.jpg?raw=true",
        "map_lat": "37.9836",
        "map_lng": "23.7312",
        "map_gmaps": "https://www.google.com/maps/place/National+Archaeological+Museum,+Athens,+Greece/@37.9836,23.7312,17z",
        "activities": [
            {
                "time": "09:00",
                "icon": "History",
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
                "icon": "Users",
                "title": "Barrio de Exarchia",
                "description": "El corazón intelectual y rebelde de Atenas. Grafitis de museo, librerías de segunda mano y la mejor música alternativa.",
                "tip": "Es un barrio progresista y seguro. Perfecto para tomar café y observar la vida local.",
                "links": [
                    {"label": "Exarchia en Maps", "url": "https://www.google.com/maps/place/Exarcheia,+Athens,+Greece"}
                ]
            },
            {
                "time": "18:00",
                "icon": "Sun",
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
                "icon": "Sparkles",
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
        "hero_image": "https://github.com/josecarlostejedor/AtenasJC/blob/main/meteora.jpg?raw=true",
        "map_lat": "39.7217",
        "map_lng": "21.6306",
        "map_gmaps": "https://www.google.com/maps/place/Meteora,+Kalambaka,+Greece/@39.7217,21.6306,14z",
        "activities": [
            {
                "time": "06:00",
                "icon": "Car",
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
                "icon": "Church",
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
                "icon": "Flower",
                "title": "Monasterio de Roussanou",
                "description": "Regentado por monjas. El más fotogénico por su posición y sus jardines en flor. Las vistas desde su terraza son las más dramáticas de Meteora.",
                "tip": "El acceso es por un puente de madera sobre el vacío. Impresionante.",
                "links": [
                    {"label": "Roussanou en Maps", "url": "https://www.google.com/maps/place/Monastery+of+Roussanou,+Meteora,+Greece"}
                ]
            },
            {
                "time": "14:30",
                "icon": "Beef",
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
        "hero_image": "https://github.com/josecarlostejedor/AtenasJC/blob/main/corazon.jpg?raw=true",
        "map_lat": "37.9715",
        "map_lng": "23.7257",
        "map_gmaps": "https://www.google.com/maps/place/Acropolis+of+Athens,+Greece/@37.9715,23.7257,17z",
        "activities": [
            {
                "time": "08:00",
                "icon": "Landmark",
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
                "icon": "History",
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
                "icon": "Home",
                "title": "Anafiótika — El barrio-isla",
                "description": "Un rincón secreto en la ladera de la Acrópolis que parece una isla de las Cícladas. Casitas blancas, gatos y silencio total.",
                "tip": "Muy pocas personas saben de este barrio. El contraste perfecto con el caos de Plaka.",
                "links": [
                    {"label": "Anafiótika en Maps", "url": "https://www.google.com/maps/place/Anafiotika,+Athens,+Greece"}
                ]
            },
            {
                "time": "17:00",
                "icon": "ShoppingBag",
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
        "hero_image": "https://github.com/josecarlostejedor/AtenasJC/blob/main/despedida.jpg?raw=true",
        "map_lat": "37.9682",
        "map_lng": "23.7412",
        "map_gmaps": "https://www.google.com/maps/place/Panathenaic+Stadium,+Athens,+Greece/@37.9682,23.7412,17z",
        "activities": [
            {
                "time": "09:00",
                "icon": "Trophy",
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
                "icon": "Landmark",
                "title": "Templo de Zeus Olímpico",
                "description": "17 columnas corintias de 17 metros de altura. El templo más grande de la antigua Grecia. A 5 minutos a pie del Estadio.",
                "tip": "La entrada combinada con la Acrópolis es más económica si no la has usado aún.",
                "links": [
                    {"label": "Templo Zeus en Maps", "url": "https://www.google.com/maps/place/Temple+of+Olympian+Zeus,+Athens,+Greece"}
                ]
            },
            {
                "time": "11:00",
                "icon": "Shield",
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
                "icon": "PlaneTakeoff",
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
  ];

  // API Route
  app.get("/api/itinerary", (req, res) => {
    res.json(ITINERARY);
  });

  // Vite middleware for development
  if (process.env.NODE_ENV !== "production") {
    const vite = await createViteServer({
      server: { middlewareMode: true },
      appType: "spa",
    });
    app.use(vite.middlewares);
  } else {
    const distPath = path.join(process.cwd(), 'dist');
    app.use(express.static(distPath));
    app.get('*', (req, res) => {
      res.sendFile(path.join(distPath, 'index.html'));
    });
  }

  app.listen(PORT, "0.0.0.0", () => {
    console.log(`Server running on http://localhost:${PORT}`);
  });
}

startServer();

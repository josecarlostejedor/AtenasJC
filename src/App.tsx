import React, { useEffect, useState } from 'react';
import { motion, AnimatePresence } from 'motion/react';
import { 
  PlaneLanding, 
  PlaneTakeoff, 
  MapPin, 
  Utensils, 
  UtensilsCrossed, 
  Car, 
  Landmark, 
  Flame, 
  History, 
  Users, 
  Sun, 
  Sparkles, 
  Mountain, 
  Church, 
  Flower, 
  Beef, 
  Home, 
  ShoppingBag, 
  Trophy, 
  Shield,
  ChevronDown,
  ExternalLink,
  Lightbulb,
  Footprints
} from 'lucide-react';
import { Day, Activity } from './types';

const IconMap: Record<string, React.ElementType> = {
  PlaneLanding,
  PlaneTakeoff,
  MapPin,
  Utensils,
  UtensilsCrossed,
  Car,
  Landmark,
  Flame,
  History,
  Users,
  Sun,
  Sparkles,
  Mountain,
  Church,
  Flower,
  Beef,
  Home,
  ShoppingBag,
  Trophy,
  Shield,
  Walk: Footprints
};

const ActivityCard: React.FC<{ activity: Activity }> = ({ activity }) => {
  const Icon = IconMap[activity.icon] || MapPin;

  return (
    <motion.div 
      initial={{ opacity: 0, y: 20 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true }}
      className="grid grid-cols-[60px_1fr] md:grid-cols-[80px_1fr] relative group"
    >
      <div className="absolute left-[30px] md:left-[40px] top-[44px] bottom-[-1.5rem] w-px bg-gold/25 group-last:hidden" />
      
      <div className="text-center pt-3 z-10">
        <div className="w-10 h-10 md:w-12 md:h-12 bg-dark border border-gold/30 flex items-center justify-center rounded-full mx-auto mb-1">
          <Icon className="w-5 h-5 md:w-6 md:h-6 text-gold" />
        </div>
        <span className="text-[10px] md:text-[11px] tracking-widest text-gold uppercase block">{activity.time}</span>
      </div>

      <div className="bg-white/5 border border-gold/20 border-l-4 border-l-gold p-5 md:p-6 ml-4 transition-colors hover:bg-white/10">
        <h4 className="font-serif text-xl md:text-2xl font-semibold mb-2">{activity.title}</h4>
        <p className="text-sm md:text-base leading-relaxed text-cream/70 mb-4">{activity.description}</p>
        
        <div className="text-[13px] md:text-[14px] text-gold bg-gold/10 border-l-2 border-l-gold p-3 mb-4 italic flex gap-2">
          <Lightbulb className="w-4 h-4 shrink-0 mt-0.5" />
          <span>{activity.tip}</span>
        </div>

        <div className="flex flex-wrap gap-2">
          {activity.links.map((link, i) => (
            <a 
              key={i}
              href={link.url}
              target="_blank"
              rel="noopener noreferrer"
              className="text-[10px] md:text-[11px] tracking-widest uppercase text-gold border border-gold/40 px-3 py-1.5 flex items-center gap-1.5 transition-all hover:bg-gold hover:text-dark"
            >
              {link.label} <ExternalLink className="w-3 h-3" />
            </a>
          ))}
        </div>
      </div>
    </motion.div>
  );
};

const DaySection: React.FC<{ day: Day }> = ({ day }) => {
  const [isMapOpen, setIsMapOpen] = useState(false);

  return (
    <section id={`dia-${day.day}`} className="max-w-5xl mx-auto py-16 md:py-24 px-6 border-t border-gold/20 first:border-t-0">
      <div className="grid md:grid-cols-[auto_1fr] gap-8 items-start mb-12">
        <div className="font-serif text-7xl md:text-9xl font-light leading-none text-gold/15 select-none">
          0{day.day}
        </div>
        <div>
          <span className="text-[11px] tracking-[0.4em] uppercase text-gold mb-2 block">{day.date}</span>
          <h2 className="font-serif text-4xl md:text-6xl font-normal leading-tight">
            <span className="mr-4">{day.emoji}</span>
            {day.title}
          </h2>
          <div className="text-[12px] md:text-[13px] tracking-[0.25em] text-cream/45 uppercase mt-3 flex items-center gap-2">
            <MapPin className="w-3 h-3 text-gold" /> {day.location}
          </div>
        </div>
      </div>

      <motion.img 
        initial={{ opacity: 0, scale: 0.95 }}
        whileInView={{ opacity: 1, scale: 1 }}
        viewport={{ once: true }}
        src={day.hero_image} 
        alt={day.title}
        referrerPolicy="no-referrer"
        className="w-full h-[300px] md:h-[450px] object-cover mb-12 filter brightness-90 saturate-90 hover:brightness-100 hover:saturate-100 transition-all duration-500"
      />

      <div className="space-y-6">
        {day.activities.map((act, i) => (
          <ActivityCard key={i} activity={act} />
        ))}
      </div>

      <div className="mt-12">
        <button 
          onClick={() => setIsMapOpen(!isMapOpen)}
          className="flex items-center gap-3 text-[12px] tracking-[0.25em] uppercase text-cream/50 hover:text-gold transition-colors py-4 border-t border-gold/20 w-full text-left"
        >
          <ChevronDown className={`w-5 h-5 transition-transform duration-300 ${isMapOpen ? 'rotate-180' : ''}`} />
          Ver mapa — {day.location}
        </button>
        
        <AnimatePresence>
          {isMapOpen && (
            <motion.div 
              initial={{ height: 0, opacity: 0 }}
              animate={{ height: 'auto', opacity: 1 }}
              exit={{ height: 0, opacity: 0 }}
              className="overflow-hidden"
            >
              <iframe
                className="w-full h-[400px] border border-gold/25 mt-4"
                loading="lazy"
                allowFullScreen
                referrerPolicy="no-referrer-when-downgrade"
                src={`https://maps.google.com/maps?q=${day.map_lat},${day.map_lng}&z=14&output=embed&hl=es`}
                title={`Mapa ${day.location}`}
              />
              <a 
                href={day.map_gmaps}
                target="_blank" 
                rel="noopener noreferrer"
                className="inline-block mt-4 text-[11px] tracking-widest uppercase text-gold border-b border-gold/40 pb-0.5 hover:border-gold transition-colors"
              >
                ↗ Abrir en Google Maps
              </a>
            </motion.div>
          )}
        </AnimatePresence>
      </div>
    </section>
  );
};

const ITINERARY_DATA: Day[] = [
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

export default function App() {
  const [itinerary] = useState<Day[]>(ITINERARY_DATA);
  const [loading] = useState(false);

  if (loading) {
    return (
      <div className="min-h-screen bg-dark flex items-center justify-center">
        <motion.div 
          animate={{ opacity: [0.4, 1, 0.4] }} 
          transition={{ duration: 2, repeat: Infinity }}
          className="font-serif text-3xl text-gold"
        >
          Cargando Itinerario...
        </motion.div>
      </div>
    );
  }

  return (
    <div className="min-h-screen selection:bg-gold selection:text-dark">
      {/* Hero Section */}
      <section className="relative min-h-screen flex flex-col items-center justify-center text-center p-8 overflow-hidden">
        <div 
          className="absolute inset-0 bg-[url('https://github.com/josecarlostejedor/AtenasJC/blob/main/aterrizaje.jpg?raw=true')] bg-center bg-cover filter brightness-[0.25] saturate-[0.7]"
        />
        <div className="absolute inset-0 bg-gradient-to-b from-transparent via-transparent to-dark" />
        
        <div className="relative z-10 max-w-4xl">
          <motion.p 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.2 }}
            className="text-[12px] tracking-[0.4em] text-gold uppercase mb-6"
          >
            Viaje · Madrid → Atenas
          </motion.p>
          <motion.h1 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.4 }}
            className="font-serif text-5xl md:text-8xl font-light leading-[1.05] mb-6"
          >
            Atenas & Meteora<br />
            <span className="text-2xl md:text-4xl text-gold/80 block mt-4 font-sans tracking-widest uppercase">
              (Familia Tejedor Cubo by JC)
            </span>
          </motion.h1>
          <motion.p 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.6 }}
            className="text-[13px] md:text-[14px] tracking-[0.3em] text-cream/60 uppercase"
          >
            6 días · 6 noches · Semana Santa en Grecia
          </motion.p>
          
          <motion.div 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.8 }}
            className="flex flex-wrap gap-4 md:gap-8 justify-center mt-12"
          >
            <div className="bg-dark/50 backdrop-blur-md border border-gold/25 p-4 md:p-6 min-w-[120px]">
              <div className="font-serif text-4xl text-gold leading-none">02</div>
              <div className="text-[10px] tracking-widest uppercase text-cream/50 mt-1">Llegada</div>
            </div>
            <div className="bg-dark/50 backdrop-blur-md border border-gold/25 p-4 md:p-6 min-w-[120px]">
              <div className="font-serif text-4xl text-gold leading-none">ABR</div>
              <div className="text-[10px] tracking-widest uppercase text-cream/50 mt-1">2026</div>
            </div>
            <div className="bg-dark/50 backdrop-blur-md border border-gold/25 p-4 md:p-6 min-w-[120px]">
              <div className="font-serif text-4xl text-gold leading-none">07</div>
              <div className="text-[10px] tracking-widest uppercase text-cream/50 mt-1">Vuelta</div>
            </div>
          </motion.div>
        </div>

        <motion.div 
          animate={{ y: [0, 10, 0] }}
          transition={{ duration: 2, repeat: Infinity }}
          className="absolute bottom-8 left-1/2 -translate-x-1/2 flex flex-col items-center gap-2"
        >
          <span className="text-[11px] tracking-[0.3em] text-cream/40 uppercase">Explorar</span>
          <div className="w-px h-12 bg-gradient-to-b from-gold to-transparent" />
        </motion.div>
      </section>

      {/* Navigation */}
      <nav className="sticky top-0 z-50 bg-dark/95 backdrop-blur-xl border-b border-gold/25 px-6 h-16 flex items-center justify-between">
        <span className="font-serif text-lg text-gold tracking-wider">Atenas & Meteora (Familia Tejedor Cubo by JC)</span>
        <div className="hidden md:flex gap-2">
          {itinerary.map(day => (
            <a 
              key={day.day}
              href={`#dia-${day.day}`}
              className="w-9 h-9 border border-gold/25 flex items-center justify-center text-[12px] text-cream/50 hover:border-gold hover:text-gold transition-all"
            >
              {day.day}
            </a>
          ))}
        </div>
      </nav>

      {/* Itinerary Sections */}
      <main>
        {itinerary.map(day => (
          <DaySection key={day.day} day={day} />
        ))}
      </main>

      {/* Summary Table */}
      <section className="max-w-5xl mx-auto py-16 px-6 border-t border-gold/20">
        <h2 className="font-serif text-3xl md:text-4xl font-light text-gold mb-12">Resumen del Itinerario</h2>
        <div className="overflow-x-auto">
          <table className="w-full text-left border-collapse text-[13px] md:text-[14px]">
            <thead>
              <tr className="border-b border-gold/25">
                <th className="py-4 px-4 text-[11px] tracking-[0.3em] uppercase text-gold font-normal">Día</th>
                <th className="py-4 px-4 text-[11px] tracking-[0.3em] uppercase text-gold font-normal">Fecha</th>
                <th className="py-4 px-4 text-[11px] tracking-[0.3em] uppercase text-gold font-normal">Ubicación</th>
                <th className="py-4 px-4 text-[11px] tracking-[0.3em] uppercase text-gold font-normal">Actividad Clave</th>
              </tr>
            </thead>
            <tbody>
              {itinerary.map(day => (
                <tr key={day.day} className="border-b border-gold/10 hover:bg-white/5 transition-colors">
                  <td className="py-4 px-4">
                    <span className="bg-gold/15 text-gold px-2 py-1 text-[11px] tracking-widest">DÍA {day.day}</span>
                  </td>
                  <td className="py-4 px-4 text-cream/80">{day.date}</td>
                  <td className="py-4 px-4 text-cream/80">{day.location}</td>
                  <td className="py-4 px-4 text-cream/80">{day.activities[0].title}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>

      {/* Tips Section */}
      <section className="max-w-5xl mx-auto py-16 px-6 border-t border-gold/20">
        <h2 className="font-serif text-3xl md:text-4xl font-light text-gold mb-12">Consejos Esenciales</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {[
            { icon: "👟", title: "Calzado", text: "El mármol de la Acrópolis y Delfos es pulido y resbala. Lleva zapatillas con buen agarre. Nunca tacones." },
            { icon: "📱", title: "App Beat (Taxi)", text: "Es el Uber griego. Descárgala antes de ir. Evita tarifas infladas al aeropuerto y en zonas turísticas." },
            { icon: "🚗", title: "Transporte a Meteora", text: "El tren Atenas–Kalambaka en 1ª clase es cómodo y pintoresco. Hay tours privados con guía incluido." },
            { icon: "🏛️", title: "Entradas Anticipadas", text: "Compra siempre online en etickets.tap.gr. La Acrópolis puede tener colas de 1 hora. Entra en la apertura." },
            { icon: "🧥", title: "Código de Vestimenta", text: "En los monasterios de Meteora: rodillas y hombros cubiertos. Ofrecen pañuelos en la entrada." },
            { icon: "☕", title: "Freddo Espresso", text: "El café nacional moderno de Grecia. Espresso batido con hielo. Pídelo 'skéto' (sin azúcar) o 'glikó' (dulce)." },
          ].map((tip, i) => (
            <motion.div 
              key={i}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              className="border border-gold/20 p-6 bg-white/2 hover:bg-white/5 transition-colors"
            >
              <div className="text-3xl mb-4">{tip.icon}</div>
              <h3 className="font-serif text-xl mb-2">{tip.title}</h3>
              <p className="text-sm leading-relaxed text-cream/65">{tip.text}</p>
            </motion.div>
          ))}
        </div>
      </section>

      <footer className="text-center py-12 px-6 border-t border-gold/20 text-[11px] tracking-[0.2em] text-cream/25 uppercase leading-loose">
        Viaje de Madrid a Atenas &middot; Semana Santa 2026 &middot; 2&ndash;7 Abril
        <br />
        App creada por <strong className="text-gold tracking-[0.15em]">JC Tejedor</strong> para su viaje inolvidable
      </footer>
    </div>
  );
}

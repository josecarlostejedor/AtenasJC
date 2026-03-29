# 🏛️ Atenas & Meteora — Itinerario Semana Santa 2026

Web con el itinerario completo del viaje Madrid → Atenas (2–7 Abril 2026).

## 🚀 Despliegue en Render (gratis)

1. Sube este repositorio a GitHub
2. Ve a [render.com](https://render.com) y crea una cuenta gratuita
3. Clic en **New → Web Service**
4. Conecta tu repositorio de GitHub
5. Configura:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Environment:** Python 3
6. Clic en **Deploy** → ¡En 2 minutos tienes tu web online!

## 💻 Ejecutar en local

```bash
pip install -r requirements.txt
python app.py
```
Abre [http://localhost:5000](http://localhost:5000)

## 📁 Archivos

- `app.py` — Aplicación Flask con todo el itinerario y la web completa
- `requirements.txt` — Dependencias Python

## ✨ Características

- Itinerario día a día con horarios detallados
- Fotos de cada destino (Unsplash)
- Mapas de Google integrados (desplegables)
- Enlaces a entradas, mapas y recursos
- Tabla resumen y consejos esenciales
- Diseño elegante responsive (móvil y escritorio)

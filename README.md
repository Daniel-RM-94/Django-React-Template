# Web T Project

Aplicación web full-stack desarrollada con Django (backend) y React (frontend).

## Estructura del Proyecto

```
Web_T_Project/
├── backend/                 # Backend Django
│   ├── manage.py
│   ├── requirements.txt
│   ├── .env.example
│   ├── .gitignore
│   └── web_t_project/      # Proyecto Django principal
│       ├── __init__.py
│       ├── settings.py
│       ├── urls.py
│       ├── wsgi.py
│       └── asgi.py
│   └── apps/               # Aplicaciones Django
│       └── api/            # API REST
│           ├── __init__.py
│           ├── models.py
│           ├── serializers.py
│           ├── views.py
│           └── urls.py
├── frontend/               # Frontend React
│   ├── package.json
│   ├── .env.example
│   ├── .gitignore
│   ├── public/
│   │   ├── index.html
│   │   └── favicon.ico
│   └── src/
│       ├── components/
│       ├── pages/
│       ├── services/
│       ├── utils/
│       ├── styles/
│       ├── App.js
│       └── index.js
├── docs/                   # Documentación
├── scripts/                # Scripts de desarrollo
└── README.md
```

## Tecnologías

- **Backend**: Django 5.2.4, Django REST Framework
- **Frontend**: React 18.3.0, Vite
- **Base de Datos**: SQLite (desarrollo) / PostgreSQL (producción)

## Instalación y Configuración

### Backend (Django)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

**Nota**: Django 5.0.2 requiere Python 3.10 o superior. El proyecto está configurado para usar un ambiente virtual que aísla las dependencias del sistema.

### Frontend (React)

```bash
cd frontend
npm install
npm run dev
```

## Desarrollo

- El backend corre en `http://localhost:8000`
- El frontend corre en `http://localhost:5173`
- La API estará disponible en `http://localhost:8000/api/` 
# Documentación del Proyecto

## Descripción General

Este proyecto es una aplicación web full-stack desarrollada con Django (backend) y React (frontend).

## Arquitectura

### Backend (Django)
- **Framework**: Django 5.2.4
- **API**: Django REST Framework
- **Base de Datos**: SQLite (desarrollo) / PostgreSQL (producción)
- **Autenticación**: Sistema de autenticación de Django

### Frontend (React)
- **Framework**: React 18.3.1
- **Bundler**: Vite
- **Routing**: React Router DOM
- **HTTP Client**: Axios

## Estructura de Carpetas

```
Web_T_Project/
├── backend/                 # Backend Django
│   ├── manage.py           # Script de administración de Django
│   ├── requirements.txt    # Dependencias de Python
│   ├── env.example         # Variables de entorno de ejemplo
│   ├── .gitignore          # Archivos a ignorar por Git
│   ├── core/      # Configuración principal de Django
│   └── apps/               # Aplicaciones Django
│       └── api/            # API REST
├── frontend/               # Frontend React
│   ├── package.json        # Dependencias de Node.js
│   ├── vite.config.js      # Configuración de Vite
│   ├── env.example         # Variables de entorno de ejemplo
│   ├── .gitignore          # Archivos a ignorar por Git
│   ├── public/             # Archivos públicos
│   └── src/                # Código fuente de React
├── docs/                   # Documentación
└── scripts/                # Scripts de desarrollo
```

## Guías de Desarrollo

### Configuración Inicial

1. **Backend**:
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   pip install -r requirements.txt
   cp env.example .env
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
   ```

2. **Frontend**:
   ```bash
   cd frontend
   npm install
   cp env.example .env
   npm run dev
   ```

### Convenciones de Código

- **Python**: PEP 8
- **JavaScript**: ESLint con configuración estándar
- **Commits**: Conventional Commits
- **Branches**: Git Flow

### Endpoints de la API

- `GET /api/` - Información general de la API
- `GET /api/examples/` - Lista de ejemplos
- `POST /api/examples/` - Crear nuevo ejemplo
- `GET /api/examples/{id}/` - Obtener ejemplo específico
- `PUT /api/examples/{id}/` - Actualizar ejemplo
- `DELETE /api/examples/{id}/` - Eliminar ejemplo

## Despliegue

### Desarrollo
- Backend: `http://localhost:8000`
- Frontend: `http://localhost:5173`
- Admin: `http://localhost:8000/admin/`

### Producción
- Configurar variables de entorno
- Usar PostgreSQL como base de datos
- Configurar servidor web (Nginx + Gunicorn)
- Configurar CDN para archivos estáticos 
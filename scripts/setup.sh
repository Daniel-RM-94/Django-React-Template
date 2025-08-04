#!/bin/bash

# Script de configuración inicial para Web T Project
echo "🚀 Configurando Core Project..."

# Configurar backend
echo "📦 Configurando backend (Django)..."
cd backend

# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# Actualizar pip
pip install --upgrade pip

# Instalar dependencias
pip install -r requirements.txt

# Verificar versión de Django
echo "Verificando versión de Django..."
python -c "import django; print('Django version:', django.get_version())"

# Configurar variables de entorno
if [ ! -f .env ]; then
    cp env.example .env
    echo "✅ Archivo .env creado en backend/"
fi

# Ejecutar migraciones
python manage.py migrate

echo "✅ Backend configurado correctamente"

# Configurar frontend
echo "📦 Configurando frontend (React)..."
cd ../frontend

# Instalar dependencias
npm install

# Configurar variables de entorno
if [ ! -f .env ]; then
    cp env.example .env
    echo "✅ Archivo .env creado en frontend/"
fi

echo "✅ Frontend configurado correctamente"

echo "🎉 ¡Configuración completada!"
echo ""
echo "Para iniciar el desarrollo:"
echo "1. Backend: cd backend && source venv/bin/activate && python manage.py runserver"
echo "2. Frontend: cd frontend && npm run dev"
echo ""
echo "URLs:"
echo "- Backend: http://localhost:8000"
echo "- Frontend: http://localhost:5173"
echo "- Admin: http://localhost:8000/admin/" 
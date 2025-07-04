@echo off

REM Script de configuración inicial para Web T Project (Windows)
echo 🚀 Configurando Web T Project...

REM Configurar backend
echo 📦 Configurando backend (Django)...
cd backend

REM Crear entorno virtual
python -m venv venv
call venv\Scripts\activate.bat

REM Actualizar pip
pip install --upgrade pip

REM Instalar dependencias
pip install -r requirements.txt

REM Verificar versión de Django
echo Verificando versión de Django...
python -c "import django; print('Django version:', django.get_version())"

REM Configurar variables de entorno
if not exist .env (
    copy env.example .env
    echo ✅ Archivo .env creado en backend/
)

REM Ejecutar migraciones
python manage.py migrate

echo ✅ Backend configurado correctamente

REM Configurar frontend
echo 📦 Configurando frontend (React)...
cd ..\frontend

REM Instalar dependencias
npm install

REM Configurar variables de entorno
if not exist .env (
    copy env.example .env
    echo ✅ Archivo .env creado en frontend/
)

echo ✅ Frontend configurado correctamente

echo 🎉 ¡Configuración completada!
echo.
echo Para iniciar el desarrollo:
echo 1. Backend: cd backend ^&^& venv\Scripts\activate ^&^& python manage.py runserver
echo 2. Frontend: cd frontend ^&^& npm run dev
echo.
echo URLs:
echo - Backend: http://localhost:8000
echo - Frontend: http://localhost:5173
echo - Admin: http://localhost:8000/admin/

pause 
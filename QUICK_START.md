# 🚀 Inicio Rápido - Web T Project

## Configuración Automática

### Windows
```bash
scripts/setup.bat
```

### Linux/Mac
```bash
bash scripts/setup.sh
```

## Configuración Manual

### 1. Backend (Django 5.0.2)

```bash
# Navegar al directorio backend
cd backend

# Crear ambiente virtual
python -m venv venv

# Activar ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Actualizar pip
pip install --upgrade pip

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
cp env.example .env

# Ejecutar migraciones
python manage.py migrate

# Crear superusuario (opcional)
python manage.py createsuperuser

# Iniciar servidor
python manage.py runserver
```

### 2. Frontend (React)

```bash
# En otra terminal, navegar al directorio frontend
cd frontend

# Instalar dependencias
npm install

# Configurar variables de entorno
cp env.example .env

# Iniciar servidor de desarrollo
npm run dev
```

## Verificación

### Verificar Backend
```bash
cd backend
# Activar ambiente virtual si no está activado
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Verificar versión de Django
python -c "import django; print(django.get_version())"
# Debería mostrar: 5.0.2

# Verificar configuración completa
python ../scripts/check_env.py
```

### URLs de Desarrollo
- **Backend**: http://localhost:8000
- **Frontend**: http://localhost:5173
- **API**: http://localhost:8000/api/
- **Admin**: http://localhost:8000/admin/

## Requisitos del Sistema

- **Python**: 3.10 o superior
- **Node.js**: 16 o superior
- **npm**: 8 o superior

## Solución de Problemas

### Error: "python no se reconoce"
- Instala Python desde https://python.org
- Asegúrate de marcar "Add Python to PATH" durante la instalación

### Error: "No module named 'django'"
- Verifica que el ambiente virtual esté activado
- Ejecuta: `pip install -r requirements.txt`

### Error: "npm no se reconoce"
- Instala Node.js desde https://nodejs.org

### Verificar Ambiente Virtual
```bash
# Debería mostrar la ruta del ambiente virtual
where python  # Windows
which python  # Linux/Mac
```

## Comandos Útiles

```bash
# Desactivar ambiente virtual
deactivate

# Ver dependencias instaladas
pip list

# Actualizar dependencias
pip install --upgrade -r requirements.txt

# Ejecutar tests (cuando se implementen)
python manage.py test
``` 
# Backend - Django 5.2.4

## Configuración del Ambiente Virtual

### Requisitos Previos
- Python 3.10 o superior
- pip (gestor de paquetes de Python)

### Instalación del Ambiente Virtual

#### Windows
```bash
# Navegar al directorio backend
cd backend

# Crear ambiente virtual
python -m venv venv

# Activar ambiente virtual
venv\Scripts\activate

# Verificar que está activado (debería mostrar la ruta del venv)
where python
```

#### Linux/Mac
```bash
# Navegar al directorio backend
cd backend

# Crear ambiente virtual
python3 -m venv venv

# Activar ambiente virtual
source venv/bin/activate

# Verificar que está activado (debería mostrar la ruta del venv)
which python
```

### Instalación de Dependencias

Una vez activado el ambiente virtual:

```bash
# Actualizar pip
pip install --upgrade pip

# Instalar dependencias
pip install -r requirements.txt
```

### Configuración del Proyecto

```bash
# Copiar archivo de variables de entorno
cp env.example .env

# Editar el archivo .env con tus configuraciones
# (opcional, los valores por defecto funcionan para desarrollo)

# Ejecutar migraciones
python manage.py migrate

# Crear superusuario (opcional)
python manage.py createsuperuser

# Ejecutar el servidor de desarrollo
python manage.py runserver
```

### Verificación de la Instalación

Para verificar que todo está funcionando correctamente:

1. **Verificar versión de Django**:
   ```bash
   python -c "import django; print(django.get_version())"
   ```
   Debería mostrar: `5.2.4`

2. **Verificar que el servidor inicia**:
   ```bash
   python manage.py runserver
   ```
   Debería mostrar: `Starting development server at http://127.0.0.1:8000/`

3. **Acceder a la API**:
   - Abrir navegador en: `http://localhost:8000/api/`
   - Debería mostrar el mensaje de bienvenida de la API

### Desactivar Ambiente Virtual

Cuando termines de trabajar:

```bash
deactivate
```

### Comandos Útiles

```bash
# Ver dependencias instaladas
pip list

# Verificar dependencias obsoletas
pip list --outdated

# Actualizar una dependencia específica
pip install --upgrade nombre-del-paquete

# Generar requirements.txt actualizado
pip freeze > requirements.txt

# Ejecutar tests (cuando se implementen)
python manage.py test

# Crear migraciones para cambios en modelos
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Acceder al shell de Django
python manage.py shell
```

### Solución de Problemas

#### Error: "python no se reconoce como comando"
- Asegúrate de que Python esté instalado y en el PATH
- En Windows, intenta usar `py` en lugar de `python`

#### Error: "pip no se reconoce como comando"
- Instala pip: `python -m ensurepip --upgrade`
- O descarga get-pip.py y ejecútalo

#### Error: "No module named 'django'"
- Asegúrate de que el ambiente virtual esté activado
- Verifica que las dependencias se instalaron: `pip list`

#### Error de permisos en Linux/Mac
- Usa `sudo` solo si es necesario para instalar Python
- No uses `sudo` para pip install dentro del ambiente virtual

### Estructura del Proyecto

```
backend/
├── venv/                    # Ambiente virtual (no versionado)
├── manage.py               # Script de administración de Django
├── requirements.txt        # Dependencias de Python
├── env.example            # Variables de entorno de ejemplo
├── .env                   # Variables de entorno (crear desde env.example)
├── .gitignore             # Archivos a ignorar por Git
├── web_t_project/         # Configuración principal de Django
│   ├── __init__.py
│   ├── settings.py        # Configuración del proyecto
│   ├── urls.py            # URLs principales
│   ├── wsgi.py            # Configuración WSGI
│   └── asgi.py            # Configuración ASGI
└── apps/                  # Aplicaciones Django
    └── api/               # API REST
        ├── __init__.py
        ├── models.py      # Modelos de datos
        ├── serializers.py # Serializers para API
        ├── views.py       # Vistas de la API
        └── urls.py        # URLs de la API
``` 
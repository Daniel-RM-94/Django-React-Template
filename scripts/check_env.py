#!/usr/bin/env python3
"""
Script para verificar la configuración del ambiente virtual de Django.
"""

import sys
import subprocess
import os

def check_python_version():
    """Verificar que la versión de Python sea compatible."""
    version = sys.version_info
    print(f"Python version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 10):
        print("❌ Error: Se requiere Python 3.10 o superior")
        return False
    else:
        print("✅ Versión de Python compatible")
        return True

def check_virtual_environment():
    """Verificar que estamos en un ambiente virtual."""
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("✅ Ambiente virtual activado")
        print(f"   Ambiente virtual: {sys.prefix}")
        return True
    else:
        print("❌ Error: No estás en un ambiente virtual")
        print("   Activa el ambiente virtual con:")
        print("   - Windows: venv\\Scripts\\activate")
        print("   - Linux/Mac: source venv/bin/activate")
        return False

def check_django_installation():
    """Verificar la instalación de Django."""
    try:
        import django
        print(f"✅ Django instalado: {django.get_version()}")
        
        # Verificar que es la versión esperada
        expected_version = "5.0.2"
        if django.get_version() == expected_version:
            print(f"✅ Versión de Django correcta: {expected_version}")
            return True
        else:
            print(f"⚠️  Versión de Django: {django.get_version()} (esperada: {expected_version})")
            return False
    except ImportError:
        print("❌ Error: Django no está instalado")
        print("   Ejecuta: pip install -r requirements.txt")
        return False

def check_django_rest_framework():
    """Verificar la instalación de Django REST Framework."""
    try:
        import rest_framework
        print(f"✅ Django REST Framework instalado: {rest_framework.VERSION}")
        return True
    except ImportError:
        print("❌ Error: Django REST Framework no está instalado")
        return False

def check_dependencies():
    """Verificar todas las dependencias principales."""
    dependencies = [
        'django',
        'djangorestframework',
        'django_cors_headers',
        'python_decouple',
        'PIL',  # Pillow
    ]
    
    missing = []
    for dep in dependencies:
        try:
            if dep == 'PIL':
                import PIL
                print(f"✅ Pillow instalado")
            else:
                __import__(dep)
                print(f"✅ {dep} instalado")
        except ImportError:
            print(f"❌ {dep} no está instalado")
            missing.append(dep)
    
    return len(missing) == 0

def check_django_project():
    """Verificar que el proyecto Django está configurado correctamente."""
    try:
        # Intentar importar la configuración de Django
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_t_project.settings')
        import django
        django.setup()
        
        # Verificar que las aplicaciones están registradas
        from django.apps import apps
        app_configs = apps.get_app_configs()
        
        print("✅ Proyecto Django configurado correctamente")
        print(f"   Aplicaciones registradas: {len(app_configs)}")
        
        for app in app_configs:
            print(f"   - {app.name}")
        
        return True
    except Exception as e:
        print(f"❌ Error en la configuración de Django: {e}")
        return False

def main():
    """Función principal."""
    print("🔍 Verificando configuración del ambiente virtual...")
    print("=" * 50)
    
    checks = [
        check_python_version(),
        check_virtual_environment(),
        check_django_installation(),
        check_django_rest_framework(),
        check_dependencies(),
        check_django_project(),
    ]
    
    print("=" * 50)
    
    if all(checks):
        print("🎉 ¡Todas las verificaciones pasaron!")
        print("   Tu ambiente virtual está configurado correctamente.")
        print("\n   Para iniciar el servidor:")
        print("   python manage.py runserver")
    else:
        print("❌ Algunas verificaciones fallaron.")
        print("   Revisa los errores arriba y corrige los problemas.")
        sys.exit(1)

if __name__ == "__main__":
    main() 
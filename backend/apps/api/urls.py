from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Configurar el router para las vistas
router = DefaultRouter()
router.register(r'examples', views.ExampleModelViewSet)

urlpatterns = [
    path('', views.api_root, name='api-root'),
    path('', include(router.urls)),
] 
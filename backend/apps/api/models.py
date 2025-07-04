from django.db import models
from django.contrib.auth.models import User

class ExampleModel(models.Model):
    """
    Modelo de ejemplo para demostrar la funcionalidad de la API.
    """
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(blank=True, verbose_name="Descripción")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")
    is_active = models.BooleanField(default=True, verbose_name="Activo")
    
    class Meta:
        verbose_name = "Ejemplo"
        verbose_name_plural = "Ejemplos"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title 
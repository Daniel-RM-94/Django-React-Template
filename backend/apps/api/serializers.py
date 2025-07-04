from rest_framework import serializers
from .models import ExampleModel

class ExampleModelSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo ExampleModel.
    """
    class Meta:
        model = ExampleModel
        fields = ['id', 'title', 'description', 'created_at', 'updated_at', 'is_active']
        read_only_fields = ['id', 'created_at', 'updated_at'] 
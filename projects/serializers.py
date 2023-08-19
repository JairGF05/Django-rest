from rest_framework import serializers
#Importando los modelos de la aplicación projects
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'technology', 'created_at')
        #campos de solo lectura, es decir no modificables
        read_only_fields = ('created_at', )
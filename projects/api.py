from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    #consulta todos los datos del modelo models.py -> class Project
    queryset = Project.objects.all()
    #quien podrá acceder a los serializers
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer

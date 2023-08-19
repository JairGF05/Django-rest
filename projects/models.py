from django.db import models

# Create your models here.
class Project(models.Model):
    #texto corto generalmente
    title = models.CharField(max_length=200)
    #texto largo
    description = models.TextField()
    technology = models.CharField(max_length=200)
    #Agrega la fecha de creación automáticamente
    created_at = models.DateField(auto_now_add=True)
"""
    Rest-framework tiene un módulo especial que crea todas las rutas básicas, o lo que se conoce
    como el CRUD de estos. Este módulo se llama routers
"""
from rest_framework import routers
#importamos el projectViewset que se definio en projects->api.py  
from .api import ProjectViewSet

router = routers.DefaultRouter()

#utilizando el router declarado voy a definir laas rutas
#Aqui en realidad se generan 4 url's POST,DELETE, PUT Y GET
router.register('api/projects', ProjectViewSet, 'projects')

#Aun asi tengo que usar un urlpatterns 
urlpatterns = router.urls

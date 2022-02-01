from django.urls import path
from .views import Tareas
from . import views

urlpatterns = [
    path('', Tareas.as_view(), name='Tareas'),
]
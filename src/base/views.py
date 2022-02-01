from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Tarea

class Tareas(ListView):
    model = Tarea

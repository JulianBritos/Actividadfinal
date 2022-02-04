from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login 


from .models import Tarea

class Iniciar_sesion(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('Tareas')

class Crear_usuario(FormView):
    template_name = 'base/Crear_usuario.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('Tareas')

    def form_valid(self, form):
        usuario = form.save()
        if usuario is not None:
            login(self.request, user)
        return super(Crear_usuario, self).form_valid(form)



class Tareas(LoginRequiredMixin, ListView):
    model = Tarea
    context_object_name = 'Tareas'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tareas'] = context['Tareas'].filter(usuario=self.request.user)
        context['count'] = context['Tareas'].filter(estado=False).count()
        return context

class Detalle_tarea(LoginRequiredMixin, DetailView):
    model = Tarea
    context_object_name = 'tarea'
    template_name = 'base/Tarea.html'

class Crear_tarea(LoginRequiredMixin, CreateView):
    model = Tarea 
    fields = ['titulo', 'descripcion', 'estado']
    success_url = reverse_lazy('Tareas')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super(Crear_tarea, self).form_valid(form)

class Editar_tarea(LoginRequiredMixin, UpdateView):
    model = Tarea
    fields = ['titulo', 'descripcion', 'estado']
    success_url = reverse_lazy('Tareas')

class Borrar_tarea(LoginRequiredMixin, DeleteView):
    model = Tarea
    context_object_name = 'tarea'
    success_url = reverse_lazy('Tareas')


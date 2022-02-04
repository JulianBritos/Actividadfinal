from django.urls import path
from .views import Tareas, Detalle_tarea, Crear_tarea, Editar_tarea, Borrar_tarea, Iniciar_sesion, Crear_usuario
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', Iniciar_sesion.as_view(), name='Login'),
    path('logout/', LogoutView.as_view(next_page='Login'), name='Logout'),
    path('crear_usuario/', Crear_usuario.as_view(), name='Crear_usuario'),

    path('', Tareas.as_view(), name='Tareas'),
    path('tarea/<int:pk>/', Detalle_tarea.as_view(), name='Tarea'),
    path('crear-tarea/', Crear_tarea.as_view(), name='crear-tarea'),
    path('editar-tarea/<int:pk>/', Editar_tarea.as_view(), 
         name='editar-tarea'),
    path('borrar-tarea/<int:pk>/', Borrar_tarea.as_view(), 
         name='borrar-tarea')

]
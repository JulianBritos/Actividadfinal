from django.db import models
from django.contrib.auth.models import User 

class Tarea(models.Model):
    STATUS_CHOINES = (
        ('A', 'Todo'),
        ('B', 'In Progress'),
        ('D', 'Done'),
        ('C', 'Close')
    )
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, 
                                null=True, blank=True)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(null=True, blank=True)
    estado = models.CharField('Estado', max_length=4, 
                              choices=STATUS_CHOINES, 
                              default='A')
    creadoel = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['estado']
from django.db import models

from especialidad.models import especialidad
from especialidad.models import especialidad

# Create your models here.

class doctor(models.Model):

    
    name = models.CharField(max_length=200, null=False, verbose_name="Nombre")
    especialidad = models.ForeignKey(especialidad, null= True, blank= True, on_delete=models.CASCADE )
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated= models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctores"
                
    def __str__(self):
        return self.name  
from django.db import models

# Create your models here.

class especialidad(models.Model):

    Id_espe = models.AutoField(primary_key=True, verbose_name="Id")
    especialidad = models.CharField(max_length=200, null=False, verbose_name="Especialidad")
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated= models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Especialidad"
        verbose_name_plural = "Especialidades"
                
    def __str__(self):
        return self.especialidad    
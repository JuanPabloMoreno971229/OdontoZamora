from email import message
from django.db import models
from django.forms import CharField
from doctor.models import doctor

# Create your models here.


class Cita(models.Model):

    name = models.CharField(max_length=200, null=False, verbose_name="Nombre")
    email = models.EmailField(max_length=200, null=False, verbose_name="Email")
    phone = models.IntegerField(null=False, verbose_name="Teléfono")
    date = models.DateTimeField(null=False, verbose_name="Fecha y hora")
    service = models.CharField(max_length=200, null=False, verbose_name="Servicio")
    doctor = models.ForeignKey(doctor, verbose_name=("Doctor(a)"), on_delete=models.DO_NOTHING)
    message = models.TextField(null=True, verbose_name="Mensaje")
    status=models.BooleanField(default=False, verbose_name="Atendido")
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated= models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")
    
    class Meta:
        verbose_name = "Cita"
        verbose_name_plural = "Citas"
                
    def __str__(self):
        return self.name, self.doctor

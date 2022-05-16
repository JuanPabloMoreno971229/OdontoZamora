from email import message
from turtle import update
from django.db import models
from django.forms import CharField

# Create your models here.

class Contacto(models.Model):
    
    name = models.CharField(max_length=200, null=False, verbose_name="Nombre")
    email = models.EmailField(max_length=200, null=False, verbose_name="Email")
    subject = models.CharField(max_length=200, null=False, verbose_name="Asunto")
    message = models.TextField(null=False, verbose_name="Mensaje")
    status=models.BooleanField(default=False, verbose_name="Contestado")
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated= models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"

    def __str__(self):
        return self.name


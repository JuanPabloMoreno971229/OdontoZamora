from pydoc import Doc, doc
from django.contrib import admin
from especialidad.models import especialidad
from .models import especialidad


# Register your models here.

# class EspecialidadAdmin(admin.ModelAdmin):
#     readonly_fields = ('name', 'especialidad','created', 'updated')
#     list_filter = ('name','especialidad')
#     list_display = ('name','especialidad')

admin.site.register(especialidad)
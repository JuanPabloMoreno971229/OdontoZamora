from distutils import core
from django.contrib import admin
from pydoc import Doc, doc
from django.contrib import admin
from core.models import servicio
from .models import servicio


# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(servicio, ServicioAdmin)

# Register your models here.
 

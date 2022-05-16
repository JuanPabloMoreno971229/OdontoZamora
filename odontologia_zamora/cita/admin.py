from django.contrib import admin
from cita.models import Cita
from .models import Cita

# Register your models here.

class CitaAdmin(admin.ModelAdmin):
    #readonly_fields = ('name', 'email', 'phone', 'date', 'service','doctor', 'message', 'created', 'updated')
    list_filter = ('doctor','status')
    list_display = ('name','doctor', 'status')

admin.site.register(Cita, CitaAdmin)
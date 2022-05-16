from django.contrib import admin
from contacto.models import Contacto
from .models import Contacto

# Register your models here.

class ContactoAdmin(admin.ModelAdmin):
    readonly_fields = ('name', 'email', 'subject', 'message','created', 'updated')
    list_filter = ('subject','status')
    list_display = ('name','subject', 'status')

admin.site.register(Contacto, ContactoAdmin)
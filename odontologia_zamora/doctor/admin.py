from pydoc import Doc, doc
from django.contrib import admin
from doctor.models import doctor
from .models import doctor


# Register your models here.

class DoctorAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_filter = ('name','especialidad')
    list_display = ('name','especialidad')

admin.site.register(doctor, DoctorAdmin)
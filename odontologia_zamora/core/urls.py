from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name="home"),
    path('cita_form/',views.cita_form, name="cita_form"),
    path('contacto_form/',views.contacto_form, name="contacto_form"),

    
]
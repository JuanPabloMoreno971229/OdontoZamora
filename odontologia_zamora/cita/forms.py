import email
from email import message
from email.policy import default
from logging import PlaceHolder
from multiprocessing.sharedctypes import Value
from pickle import TRUE
from select import select
from colorama import Style
from django import forms
from .models import Cita
from especialidad.models import especialidad
from doctor.models import doctor


class CitaForm(forms.ModelForm):

    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Nombre'}
    ))
    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(
        attrs={'class':'form-control','placeholder':'Email'}
    ))
    phone = forms.CharField(label="Teléfono", required=True, widget=forms.NumberInput(
        attrs={'class':'form-control','placeholder':'Teléfono'}
    ))
    date = forms.DateTimeField(label="Fecha", required=True, widget=forms.DateTimeInput(
        attrs={'class':'form-control datepicker', 'placeholder':'Fecha','type':'datetime-local', 'min':'08:00' ,'max':'16:00','step':'1800'}
    ))
    service = forms.ModelChoiceField(queryset=especialidad.objects.all(), empty_label="Seleccionar servicio", widget= forms.Select(
        attrs={'class':'form-select','placeholder':'Servicio'}
    ))
    doctor = forms.ModelChoiceField(queryset=doctor.objects.all(), empty_label="Seleccionar doctor", widget= forms.Select(
        attrs={'class':'form-select','placeholder':'Doctor'}
    ))
    message = forms.CharField(label="Mensaje", required=False, widget=forms.Textarea(
        attrs={'class':'form-control','placeholder':'Mensaje', 'row': 3}
    ))
    status = forms.HiddenInput( attrs={'class':'col-md-4 form-group mt-3','placeholder':'Estado'})

    class Meta:
        model = Cita
        fields = '__all__'

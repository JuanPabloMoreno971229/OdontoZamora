import email
from email import message
from pickle import TRUE
from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):

    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Nombre'}
    ))
    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(
        attrs={'class':'form-control','placeholder':'Email'}
    ))
    subject = forms.CharField(label="Asunto", required=True, widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Asunto'}
    ))
    message = forms.CharField(label="Mensaje", required=True, widget=forms.Textarea(
        attrs={'class':'form-control','placeholder':'Mensaje', 'row': 5}
    ))
    status = forms.HiddenInput( attrs={'class':'form-control','placeholder':'Estado'})

    class Meta:
        model = Contacto
        fields = '__all__'


from email import message
import imp
from datetime import date, datetime
from time import strptime
from django.shortcuts import render, redirect
from django.urls import reverse
from contacto.forms import ContactoForm
from cita.forms import CitaForm
from cita.models import Cita
from doctor.models import doctor

# Create your views here.

def home(request):
    if request.method == "POST":
          form = ContactoForm(request.POST)
          form1 = CitaForm(request.POST)
          
    else:
          form = ContactoForm()
          form1 = CitaForm()

    context = {

          "form":form,
          "form1":form1,

     }
    return render(request, "core/index.html", context)

def contacto_form(request):
       if request.method == "POST":
          form = ContactoForm(request.POST)
          if form.is_valid():
            form.save()
          else:
            form = ContactoForm()
       return redirect('home')

def cita_form(request):
       
       if request.method == "POST":
          form = CitaForm(request.POST)
          if form.is_valid():
            today = datetime.today()
            date1 = request.POST.get("date")
            date2= datetime.strptime(date1, '%Y-%m-%dT%H:%M')
            doctor1 = request.POST.get("doctor")
            doctor1 = doctor.objects.get(id=doctor1)
            print(doctor1)
            print(Cita.objects.filter(doctor = doctor1))
            if date2 < today:
              return redirect(reverse('home')+'?date-wrong')
            elif Cita.objects.filter(doctor = doctor1 ):
              print("Estoy aqui")
              if Cita.objects.filter(date=date2):
                print("Ahora aqui")
                return redirect(reverse('home')+'?#appointment')
            else:
              print("Nunca me fui")
              form.save()  
          else:
            print(form.errors.as_data())
            form = CitaForm()
       return redirect('home')  
from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request, 'index/index.html')

def perfilmedico(request):
    paciente=Pacientecli.objects.all()
    data={
        'paciente': paciente
    }
    return render(request, 'medico/perfilmedico.html', data)

def perfilpaciente(request):
    return render(request, 'paciente/perfilpaciente.html')

def historialclinico(request, id):
    paciente = Pacientecli.objects.get(id_paciente=id)
    contexto = {
        'paciente': paciente
    }
    return render(request, 'medico/historialclinicopaciente.html', contexto)


from django.db import models
from django.utils import timezone
# Create your models here.

class GeneroPaciente(models.Model):
    nombre_genero=models.CharField(max_length=9)
    
    def __str__(self):
        return self.nombre_genero

class Pacientecli(models.Model):
    id_paciente=models.AutoField(primary_key=True)
    rut=models.CharField(max_length=12)
    nombre_paciente=models.CharField(max_length=100)
    fecha_nac=models.DateField()
    genero=models.ForeignKey(GeneroPaciente, on_delete=models.SET_NULL, null=True)
    numero_telefonico=models.CharField(max_length=13)
    historial_clinico=models.TextField(default='Antecedentes Clinicos')

    def __str__(self):
        return f'{self.nombre_paciente}'

class Citas_medicas(models.Model):
    nombre_paciente=models.ForeignKey(Pacientecli, on_delete=models.SET_NULL, null=True)
    fecha_cita=models.DateField()
    hora_cita=models.TimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.nombre_paciente} - {self.fecha_cita} - {self.hora_cita}'
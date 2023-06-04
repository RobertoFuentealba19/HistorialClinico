from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', index, name="index"),
    path('perfilmedico/', perfilmedico, name="perfilmedico"),
    path('perfilpaciente/', perfilpaciente, name="perfilpaciente"),
    path('historialclinicopaciente<id>/', historialclinico, name="historialclinicopaciente"),
]
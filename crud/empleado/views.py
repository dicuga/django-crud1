from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DetailView, ListView
from .models import Empleado


class Index(TemplateView):
    
    template_name = 'empleado/index.html'


class Alta(CreateView):

    model = Empleado
    template_name_suffix = '_add_form'
    fields = ['nombre', 'apellidos']


class Detalle(DetailView):

    model = Empleado
    template_name = 'empleado/empleado_detail.html'


class EmpleadoList(ListView):
    
    model = Empleado
    context_object_name = 'empleado_list'
    queryset = Empleado.objects.filter(nombre__contains='aa')
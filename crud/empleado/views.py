from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView, ListView, UpdateView, DeleteView
from .models import Empleado


class EmpleadoCreateView(CreateView):

    model = Empleado
    # template_name_suffix = '_add_form'
    fields = ['nombre', 'apellidos','fecha_nacimiento', 'email','salario']


class EmpleadoDetailView(DetailView):

    model = Empleado
    #template_name = 'empleado/empleado_detail.html'


class EmpleadoListView(ListView):
    
    model = Empleado
    context_object_name = 'empleado_list'
    queryset = Empleado.objects.filter(nombre__contains='aa')

class EmpleadoUpdateView(UpdateView):
    
    model = Empleado


class EmpleadoDelete(DeleteView):
    
    model = Empleado
    success_url = reverse_lazy('empleado_list')


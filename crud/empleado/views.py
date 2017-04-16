from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, DetailView, ListView, UpdateView, DeleteView
from .models import Empleado


class EmpleadoCreateView(CreateView):

    model = Empleado
    fields = ['nombre', 'apellidos','fecha_nacimiento', 'email','salario']
    #reverse('empleado-detail', kwargs={'pk': self.pk})


class EmpleadoDetailView(DetailView):

    model = Empleado
    context_object_name = 'empleado'


class EmpleadoListView(ListView):
    
    model = Empleado
    context_object_name = 'empleado_list'
    queryset = Empleado.objects.filter(nombre__contains='aa')

class EmpleadoUpdateView(UpdateView):
    
    model = Empleado


class EmpleadoDelete(DeleteView):
    
    model = Empleado
    success_url = reverse_lazy('empleado-list')


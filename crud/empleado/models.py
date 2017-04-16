from django.db import models
from core.models import TimeStampedModel
from django.urls import reverse

class Empleado(TimeStampedModel):
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=60)
    email = models.EmailField(blank=True)
    salario = models.FloatField(null=True, blank=True)

    def __str__(self):
        return ' '.join([self.nombre, self.apellidos])

    def get_absolute_url(self):
        return reverse('empleado-detail', kwargs={'pk': self.pk})
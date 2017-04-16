from django.conf.urls import url
from .views import Index, Alta, Detalle, EmpleadoList

urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^alta$',Alta.as_view(), name='alta'),
    url(r'^detalle/(?P<pk>[0-9]+)$',Detalle.as_view(), name='empleado-detail'),
    url(r'^list/$',EmpleadoList.as_view(), name='empleado-list'),
]
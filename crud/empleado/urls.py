from django.conf.urls import url
from .views import EmpleadoCreateView, EmpleadoDetailView, EmpleadoListView

urlpatterns = [
    url(r'^$',EmpleadoListView.as_view(), name='empleado-list'),
    url(r'^add/$',EmpleadoCreateView.as_view(), name='empleado-add'),
    url(r'^detail/(?P<pk>[0-9]+)$',EmpleadoDetailView.as_view(), name='empleado-detail'),
]
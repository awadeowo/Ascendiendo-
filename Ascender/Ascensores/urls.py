from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from Ascensores import views

urlpatterns = [
    path('', views.home, name='home'),
    url(r'^crearOrden$', views.OrdenCreate.as_view(), name='OrdenCreate'),
    url(r'^listarOrden', views.OrdenList.as_view(), name='OrdenList'),
    url(r'^listarCliente', views.ClienteList.as_view(), name='ClienteList'),
    url(r'^CrearCliente', views.ClienteCreate.as_view(), name='ClienteCreate'),

    url(r'^modificar$', views.OrdenUpdate.as_view(), name='OrdenModificar'),
    url(r'^listarOrdenes', views.OrdenesList.as_view(), name='OrdenesList'),
    url(r'^listado', views.lista.as_view(), name='lista'),

]

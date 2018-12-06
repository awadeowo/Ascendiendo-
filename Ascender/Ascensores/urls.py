from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from Ascensores import views

urlpatterns = [
    path('', views.home, name='home'),

    url(r'^crearOrden$', views.OrdenCreate.as_view(), name='OrdenCreate'),
    url(r'^listarOrden', views.OrdenList.as_view(), name='OrdenList'),
    url(r'^listarCliente', views.ClienteList.as_view(), name='ClienteList'),
    url(r'^CrearCliente', views.ClienteCreate.as_view(), name='ClienteCreate')
    #url(r'^perrites/$', views.perros, name='perros'),
    #url(r'^agregar$', views.PerroCreate.as_view(), name='PerroCreate'),
    #url(r'^listar', views.PerroList.as_view(), name='PerroList'),
    #url(r'^disponibles', views.disponibles.as_view(), name='disponibles'),
    #url(r'^modificar/(?P<pk>\d+)/$', views.PerroUpdate.as_view(), name='PerroModificar'),
    #url(r'^eliminar/(?P<pk>\d+)/$', views.PerroDelete.as_view(), name='PerroEliminar'),
]

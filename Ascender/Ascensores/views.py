from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.views.generic.edit import FormView
from .models import ordendetrabajo, cliente
from .forms import ordenTrabajoForm, clienteForm
from Registros.models import *
# Create your views here.

def home(request):
    return render(request, 'Ascensores/homeAscensor.html', {})

class OrdenList(ListView):
        model = ordendetrabajo
        template_name = 'Ascensores/OrdenList.html'
        paginate_by = 3


class OrdenCreate(CreateView):
    model = ordendetrabajo
    form_class = ordenTrabajoForm
    template_name = 'Ascensores/OrdenCreate.html'
    success_url = reverse_lazy('OrdenList')


class ClienteList(ListView):
    model = cliente
    template_name = 'Admin/listarClientes.html'
    paginate_by = 3

class ClienteCreate(CreateView):
    model = cliente
    form_class = clienteForm
    template_name = 'Admin/CrearClientes.html'
    success_url = reverse_lazy('ClienteList')

class lista(ListView):
    model = cliente
    template_name = 'Mantenedor/listarClientes.html'


class OrdenUpdate(UpdateView):
    model = ordendetrabajo
    form_class = ordenTrabajoForm
    template_name = 'Ascensores/OrdenModificar.html'
    success_url = reverse_lazy('OrdenList')




class OrdenesList(ListView):
    model = ordendetrabajo
    template_name = 'Mantenedor/OrdenesList.html'

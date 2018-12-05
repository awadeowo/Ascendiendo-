from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.views.generic.edit import FormView
from .models import ordendetrabajo
from .forms import ordenTrabajoForm

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



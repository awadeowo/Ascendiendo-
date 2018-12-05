from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import UserCreationForm
from .models import CustomUser
# Create your views here.


def login_redirect(request):
    return redirect('/registro/login')

def registrar(request):
    mensaje = ""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(login_redirect)
        else:
            mensaje = form.errors
            return render(request, 'registro/registro.html', {'mensaje': mensaje, 'form': form})
    else:
        form = UserCreationForm()
        args = {'form': form}
        return render(request, 'registro/registro.html', args)
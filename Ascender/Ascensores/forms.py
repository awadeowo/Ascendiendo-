from django import forms
from .models import ordendetrabajo, cliente
import datetime


class clienteForm(forms.ModelForm):
    class Meta:
        model = cliente

        fields = {
            "run",
            "nombre",
            "direccion",
            "cuidad",
            "comuna",
            "telefono",
            "correo",
        }

        labels = {
            'run': 'Run Cliente',
            'nombre': 'Nombre',
            'direccion': 'Direccion',
            'cuidad': 'Ciudad',
            'comuna': 'Comuna',
            'telefono': 'Telefono',
            'correo': 'Correo',
        }



class ordenTrabajoForm(forms.ModelForm):
    class Meta:
        model = ordendetrabajo

        fields = [
            "run_cliente",
            "nombre_cliente",
            "fecha",
            "hora_ini",
            "hora_term",
            "id_ascensor",
            "modelo_ascensor",
            "descripcion_falla",
            "descripcion_reparacion",
            "piezas_cambiadas",
            "nombre_receptor_de_trabajo",
        ]

        labels = {
            'run_cliente': 'Run cliente',
            'nombre_cliente': 'Nombre Cliente',
            'fecha': 'Fecha',
            'hora_ini': 'Hora de inicio',
            'hora_term': 'Hora de termino',
            'id_ascensor': 'Id ascensor',
            'modelo_ascensor': 'Modelo ascensor',
            'descripcion_falla': 'Fallas',
            'descripcion_reparacion': 'Reparaciones',
            'piezas_cambiadas': 'Piezas cambiadas',
            'nombre_receptor_de_trabajo': 'Nombre Receptor',
        }

        now = datetime.datetime.now()
        BIRTH_YEAR_CHOICES = range(now.year-98, now.year)

        widgets = {
            'fecha': forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES),
            'hora_ini': forms.TimeInput(format="HH:MM:SS"),
            'hora_term': forms.TimeInput(format="HH:MM:SS"),
            'run_cliente': forms.Select(attrs={'class':'form-control'}),
        }
        def init(self, args, **kwargs):
            super(ordenTrabajoForm, self).init(args, **kwargs)
            self.fields['run_cliente'].queryset=cliente.objects.all()

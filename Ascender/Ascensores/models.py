from django.db import models

# Create your models here.

class cliente(models.Model):
    run = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=20, null=False)
    direccion = models.CharField(max_length=40, null=False)
    cuidad = models.CharField(max_length=30, null=False)
    comuna = models.CharField(max_length=30, null=False)
    telefono = models.CharField(max_length=30, null=False)
    correo = models.CharField(max_length=30, null=False)

class ordendetrabajo(models.Model):
    id_orden = models.AutoField(max_length=6, primary_key=True)
    run_cliente =  models.ForeignKey(cliente,on_delete=models.CASCADE)
    nombre_cliente = models.CharField(max_length=20, null=False)
    fecha = models.DateField(null=False)
    hora_ini = models.DateTimeField(null=False)
    hora_term = models.DateTimeField(null=False)
    id_ascensor = models.IntegerField(null=False)
    modelo_ascensor = models.CharField(max_length=20, null=False)
    descripcion_falla = models.CharField(max_length=300, null=True)
    descripcion_reparacion = models.CharField(max_length=300, null=True)
    piezas_cambiadas = models.CharField(max_length=200, null=True)
    nombre_receptor_de_trabajo = models.CharField(max_length=30, null=False)
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

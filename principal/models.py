
from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.utils import timezone
 



class StudentForm(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    file = models.FileField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        db_table = "student"


class Opcion(models.Model):
    nombre = models.CharField(max_length=50)

class TuModelo(models.Model):
    opciones = models.ManyToManyField('Opcion', verbose_name="Opciones")
   
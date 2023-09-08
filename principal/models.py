from django.db import models

class nuevoUsuario(models.Model):
  Documento = models.CharField(max_length=20)
  Nombre = models.CharField(max_length=30)
  Apellido = models.CharField(max_length=30)
  Clave = models.CharField(max_length=500)
  Estado = models.BooleanField()
  idRol = models.IntegerField()
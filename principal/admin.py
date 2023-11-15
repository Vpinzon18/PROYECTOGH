from django.contrib import admin
from .models import evaluaciondesempenoForm
from django.contrib.auth.models import Permission 

class evaluaciondesempenoadmin(admin.ModelAdmin):
    list_display = ('id_evaluacion', 'examenes', 'experiencia', 'educacion', 'competencias', 'suma_total', 'idUser')

admin.site.register(evaluaciondesempenoForm, evaluaciondesempenoadmin)
admin.site.register(Permission)
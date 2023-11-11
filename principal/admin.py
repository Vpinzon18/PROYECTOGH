from django.contrib import admin
from .models import evaluaciondesempenoForm

class evaluaciondesempenoadmin(admin.ModelAdmin):
    list_display = ('id_evaluacion', 'examenes', 'experiencia', 'educacion', 'competencias', 'suma_total', 'idUser')

admin.site.register(evaluaciondesempenoForm, evaluaciondesempenoadmin)

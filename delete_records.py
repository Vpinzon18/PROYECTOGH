import os
import django

# Configura las configuraciones de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'principal.settings')
django.setup()

# Importa el modelo y borra todos los registros
from principal.models import StudentForm

# Selecciona todos los registros de la tabla StudentForm y bórralos
StudentForm.objects.all().delete()

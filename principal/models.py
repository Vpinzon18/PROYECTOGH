
from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.utils import timezone
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import re
from django.utils.translation import gettext_lazy as _
 
 # Define a regular expression pattern
regex_pattern = r'\d{3}-\d{2}-\d{4}'

# Use the regex_pattern in a regular expression match
text = 'My social security number is 123-45-6789'
match = re.search(regex_pattern, text)

if match:
    print("Match found:", match.group())
else:
    print("No match found")
 
 
#  validacion para soo poder subir archivos tipo img
def validate_image_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    from django.utils.translation import gettext_lazy as _

    ext = os.path.splitext(value.name)[1].lower()
    valid_extensions = ['.jpg', '.jpeg', '.png']

    if not ext in valid_extensions:
        raise ValidationError(_('Formato de archivo no válido. Los formatos permitidos son .jpg, .jpeg y .png.'))
 
 
# Validacion para ingresar una mayuscula 
def contiene_mayuscula(value):
    if not any(char.isupper() for char in value):
        raise ValidationError('El campo debe contener al menos una letra mayúscula.')
    # Validacion para ingresar una mayuscula
def contiene_solo_letras(value):
    if not re.match(regex_pattern, value):
        raise ValidationError('El campo solo debe contener letras y espacios.')

class FormularioForm(models.Model):
    id = models.AutoField(primary_key=True)
    Documento = models.PositiveIntegerField()
    tipo_sangre = models.CharField(
        max_length=3,choices=[
            ('A+','A+'),
            ('A-', 'A-'),
            ('B+', 'B+'),
            ('B-', 'B-'),
            ('AB+', 'AB+'),
            ('AB-', 'AB-'),
            ('O+', 'O+'),
            ('O-', 'O-'),
        ]
    )
    Cargo_Actual = models.CharField(
    max_length=100,choices=[
    ("Academic Advisor", "Academic Advisor"),
    ("Analista Contable", "Analista Contable"),
    ("Analista de compensación", "Analista de compensación"),
    ("Analista de comunicaciones", "Analista de comunicaciones"),
    ("Analista de Gestión Organizacional", "Analista de Gestión Organizacional"),
    ("Asesor Servicios Integrales", "Asesor Servicios Integrales"),
    ("Asesora EduSA", "Asesora EduSA"),
    ("Asistente Académico", "Asistente Académico"),
    ("Asistente Cultural", "Asistente Cultural"),
    ("Asistente de Comunicaciones", "Asistente de Comunicaciones"),
    ("Asistente de Dirección", "Asistente de Dirección"),
    ("Asistente de Innovación y Negocios", "Asistente de Innovación y Negocios"),
    ("Asistente de Recursos Administrativos", "Asistente de Recursos Administrativos"),
    ("Asistente de servicios bibliotecarios", "Asistente de servicios bibliotecarios"),
    ("Asistente Maker", "Asistente Maker"),
    ("Aprendiz", "Aprendiz"),
    ("Auxiliar Contable", "Auxiliar Contable"),
    ("Auxiliar de mantenimiento y recursos físicos", "Auxiliar de mantenimiento y recursos físicos"),
    ("Auxiliar de Selección y contratación", "Auxiliar de Selección y contratación"),
    ("Auxiliar de seguridad", "Auxiliar de seguridad"),
    ("Auxiliar de Soporte Técnico", "Auxiliar de Soporte Técnico"),
    ("Auxiliar Tecnología Educativa", "Auxiliar Tecnología Educativa"),
    ("Coordinador académico sede sur", "Coordinador académico sede sur"),
    ("Coordinador de acompañamiento psicosocial", "Coordinador de acompañamiento psicosocial"),
    ("Coordinador de mercadeo", "Coordinador de mercadeo"),
    ("Coordinador de proyectos especiales", "Coordinador de proyectos especiales"),
    ("Coordinador de Programación y Gestión Comercial", "Coordinador de Programación y Gestión Comercial"),
    ("Coordinador de servicios STEAM y bibliotecas", "Coordinador de servicios STEAM y bibliotecas"),
    ("Coordinador sede virtual", "Coordinador sede virtual"),
    ("Coordinadora de programa Kids and Teens", "Coordinadora de programa Kids and Teens"),
    ("Coordinadora de responsabilidad social y egresados", "Coordinadora de responsabilidad social y egresados"),
    ("Coordinadora sede norte", "Coordinadora sede norte"),
    ("Desarrollador de producto", "Desarrollador de producto"),
    ("Director Cultural", "Director Cultural"),
    ("Director de Innovación y negocios", "Director de Innovación y negocios"),
    ("Director Financiero y Administrativo", "Director Financiero y Administrativo"),
    ("Director General", "Director General"),
    ("Docente", "Docente"),
    ("Jefe de Comunicaciones", "Jefe de Comunicaciones"),
    ("Jefe de Contabilidad", "Jefe de Contabilidad"),
    ("Jefe de Desarrollo de Producto", "Jefe de Desarrollo de Producto"),
    ("Jefe de Gestión Humana", "Jefe de Gestión Humana"),
    ("Jefe de Gestión Organizacional", "Jefe de Gestión Organizacional"),
    ("Jefe de mantenimiento y recursos físicos", "Jefe de mantenimiento y recursos físicos"),
    ("Jefe de Servicios Culturales", "Jefe de Servicios Culturales"),
    ("Jefe de Servicios Integrales", "Jefe de Servicios Integrales"),
    ("Recepcionista", "Recepcionista"),
    ("Subdirector académico", "Subdirector académico"),
    ("Support Teacher", "Support Teacher"),
    ("Técnico electricista", "Técnico electricista"),
    ("Técnico electrónico", "Técnico electrónico"),
    ("Conductor-mensajero", "Conductor-mensajero"),])
    Numero_Contacto = models.PositiveIntegerField()
    Numero_Emergencia = models.PositiveIntegerField()
    Fecha_Nacimiento = models.DateField()
    Departamento_Nacimiento = models.CharField(max_length=20, validators=[contiene_mayuscula])
    Ciudad_Nacimiento = models.CharField(max_length=20, validators=[contiene_mayuscula])
    Ciudad_Residencia = models.CharField(max_length=20, validators=[contiene_mayuscula])
    Direccion_Residencia = models.CharField(max_length=100, )
    Sexo = models.CharField(
        max_length=15,choices=[
            ('Masculino','Masculino'),
            ('Femenino', 'Femenino')
        ]
    )
    Estado_Civil = models.CharField(
        max_length=15,choices=[
            ('Soltero(a)','Soltero(a)'),
            ('Casado(a)', 'Casado(a)'),
            ('Union Libre', 'Union Libre'),
            ('Viudo(a)', 'Viudo(a)')
        ]
    )
    Talla_Camisa = models.CharField(
        max_length=15,choices=[
            ('XS','XS'),
            ('S','S'),
            ('M','M'),
            ('L','L'),
            ('XL','XL'),
            ('XXL','XXL'),
            ('XXXL','XXXL')
        ]
    )
    Vegetariano = models.CharField(
        max_length=2,choices=[
            ('Si','Si'),
            ('No', 'No'),
        ]
    )
    Actualmente_Tiene_Restricciones_Laborales_Por_Su_EPS = models.CharField(
        max_length=2,choices=[
            ('Si','Si'),
            ('No', 'No'),
        ]
    )
    Actualmente_Se_Encuentra_En_Perdida_De_Capacidad_Laboral = models.CharField(
        max_length=2,choices=[
            ('Si','Si'),
            ('No', 'No'),
        ]
    )
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        db_table = "Formulario"
    file = models.FileField(validators=[validate_image_file_extension])

class Opcion(models.Model):
    nombre = models.CharField(max_length=50)

class TuModelo(models.Model):
    opciones = models.ManyToManyField('Opcion', verbose_name="Opciones")
    
    
    
    
    
    
    
    
    
    
       # lastname = models.CharField(max_length=50)
    # email = models.EmailField(max_length=254)
    # fecha_creacion = models.DateTimeField(default=timezone.now)
    
    
    
    
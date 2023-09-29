
from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.utils import timezone
from django.core.validators import RegexValidator
 



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
    Departamento_Nacimiento = models.CharField(
    max_length=100,choices=[
    ('Amazonas', 'Amazonas'),
    ('Antioquia', 'Antioquia'),
    ('Arauca', 'Arauca'),
    ('Atlántico', 'Atlántico'),
    ('Bolívar', 'Bolívar'),
    ('Boyacá', 'Boyacá'),
    ('Caldas', 'Caldas'),
    ('Cauca', 'Cauca'),
    ('Caquetá', 'Caquetá'),
    ('Casanare', 'Casanare'),
    ('Cesar', 'Cesar'),
    ('Chocó', 'Chocó'),
    ('Córdoba', 'Córdoba'),
    ('Cundinamarca', 'Cundinamarca'),
    ('Guainía', 'Guainía'),
    ('Guaviare', 'Guaviare'),
    ('Huila', 'Huila'),
    ('La Guajira', 'La Guajira'),
    ('Magdalena', 'Magdalena'),
    ('Meta', 'Meta'),
    ('Nariño', 'Nariño'),
    ('Norte de Santander', 'Norte de Santander'),
    ('Quindío', 'Quindío'),
    ('Risaralda', 'Risaralda'),
    ('San Andrés y Providencia', 'San Andrés y Providencia'),
    ('Santander', 'Santander'),
    ('Sucre', 'Sucre'),
    ('Tolima', 'Tolima'),
    ('Valle del Cauca', 'Valle del Cauca'),
    ('Vaupés', 'Vaupés'),
    ('Vichada', 'Vichada'),
    ('Otros', 'Otros'),])
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
    Vegetariano = models.CharField(
        max_length=2,choices=[
            ('Si','Si'),
            ('No', 'No'),
        ]
    )
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        db_table = "Formulario"


class Opcion(models.Model):
    nombre = models.CharField(max_length=50)

class TuModelo(models.Model):
    opciones = models.ManyToManyField('Opcion', verbose_name="Opciones")
       # lastname = models.CharField(max_length=50)
    # email = models.EmailField(max_length=254)
    # file = models.FileField()
    # fecha_creacion = models.DateTimeField(default=timezone.now)
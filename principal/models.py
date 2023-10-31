
from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.utils import timezone
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import re
from django.utils.translation import gettext_lazy as _cls

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
    # Validacion para los campos numericos
    if not any(char.isupper() for char in value):
        raise ValidationError('El campo debe contener al menos una letra mayúscula.')
    # Validacion para ingresar una mayuscula
def contiene_solo_letras(value):
    if not re.match(regex_pattern, value):
        raise ValidationError('El campo solo debe contener letras y espacios.')
     # Define a regular expression pattern
regex_pattern = r'\d{3}-\d{2}-\d{4}'
# Use the regex_pattern in a regular expression match
text = 'My social security number is 123-45-6789'
match = re.search(regex_pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match found")

class formularioForm(models.Model):
    id_formulario = models.AutoField(primary_key=True)
    Documento = models.PositiveIntegerField()
    Tipo_Documento = models.CharField(
        max_length=30,choices=[
            (' Cédula de Ciudadanía', 'Cédula de Ciudadanía'),
            (' Cédula de Extranjería', 'Cédula de Extranjería'),
            (' Tarjeta de Identidad', 'Tarjeta de Identidad'),
            (' Tarjeta de Extrangeria', 'Tarjeta de Extrangeria'),
            (' NIT', 'NIT'),
            (' NIT de otro pais', 'NIT de otro pais'),
            (' NUIP', 'NUIP'),
            (' Pasaporte', 'Pasaporte'),
            (' PEP', 'PEP'),
            (' Registro Civil', 'Registro Civil'),
        ]
    )
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
    Etnia = models.CharField(
        max_length=15,choices=[
            ('Mestizo', 'Mestizo'),
            ('Afrocolombiano', 'Afrocolombiano'),
            ('Indígena', 'Indígena'),
            ('Blanco', 'Blanco'),
            ('Meztizo', 'Meztizo'),
            ('Mulato', 'Mulato'),
            ('Zambo', 'Zambo'),
            ('Raizal', 'Raizal'),
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
    Pensionado = models.CharField(
        max_length=13,choices=[
            ('Por vejez','Por vejez'),
            ('Por invalidez', 'Por invalidez'),
            ('No', 'No'),
        ]
    )
    Discapacidad_Familiar = models.CharField(
        max_length=2,choices=[
            ('Si','Si'),
            ('No', 'No'),
        ]
    )
    Tipo_Vivienda = models.CharField(
        max_length=29,choices=[
            ('Arrendada','Arrendada'),
            ('propia', 'propia'),
            ('Familiar', 'Familiar'),
            ('Compartida Con Otras Familias', 'Compartida Con Otras Familias'),
        ]
    )
    Estrato_Vivienda = models.CharField(
        max_length=2,choices=[
            ('1','1'),
            ('2','2'),
            ('3','3'),
            ('4','4'),
            ('5','5'),
            ('6','6'),
        ]
    )
    Tiempo_Desplazamiento = models.CharField(
        max_length=23,choices=[
            ('Realizo teletrabajo','Realizo teletrabajo'),
            ('Menos de 15 minutos','Menos de 15 minutos'),
            ('Entre 15 y 30 minutos','Entre 15 y 30 minutos'),
            ('Entre 30 y 45 minutos','Entre 30 y 45 minutos'),
            ('Entre 45 y 60 minutos','Entre 45 y 60 minutos'),
            ('Entre 60 y 75 minutos','Entre 60 y 75 minutos'),
            ('Entre 75 y 90 minutos','Entre 75 y 90 minutos'),
            ('Entre 90 y 120 minutos','Entre 90 y 120 minutos'),
            ('Entre 120 y 150 minutos','Entre 120 y 150 minutos'),
            ('Entre 150 y 180 minutos','Entre 150 y 180 minutos'),
            ('Entre 180 y 210 minutos','Entre 180 y 210 minutos'),
            ('Entre 210 y 240 minutos','Entre 210 y 240 minutos'),
            ('Mas de 240 minutos','Mas de 240 minutos'),
        ]
    )
    Tiempo_Vinculacion_Laboral = models.CharField(
        max_length=20,choices=[
            ('Menos de 1 año','Menos de 1 año'),
            ('de 1 a 3 años', 'de 1 a 3 años'),
            ('de 3 a 5 años', 'de 3 a 5 años'),
            ('de 5 a 10 años', 'de 5 a 10 años'),
            ('de 10 a 15 años', 'de 10 a 15 años'),
            ('de 15 a 20 años', 'de 15 a 20 años'),
            ('mas de 20 años', 'mas de 20 años'),
        ]
    )
    Tiempo_Cargo_Laboral = models.CharField(
        max_length=20,choices=[
            ('Menos de 1 año','Menos de 1 año'),
            ('de 1 a 3 años', 'de 1 a 3 años'),
            ('de 3 a 5 años', 'de 3 a 5 años'),
            ('de 5 a 10 años', 'de 5 a 10 años'),
            ('de 10 a 15 años', 'de 10 a 15 años'),
            ('de 15 a 20 años', 'de 15 a 20 años'),
            ('mas de 20 años', 'mas de 20 años'),
        ]
    )
    Nivel_Educativo_Mas_Alto = models.CharField(
        max_length=22,choices=[
            ('Bachiller','Bachiller'),
            ('Tecnico', 'Tecnico'),
            ('Tecnologo', 'Tecnologo'),
            ('Profesional/Licenciado', 'Profesional/Licenciado'),
            ('Especialista', 'Especialista'),
            ('Magister', 'Magister'),
            ('Doctorado', 'Doctorado'),
            ('Posdoctorado', 'Posdoctorado'),
            ('Ninguno', 'Ninguno'),
        ]
    )
    Ultimo_Nivel_Educativo = models.CharField(max_length=250)
    Tipo_Contrato_Form = models.CharField(
        max_length=23,choices=[
            ('Termino Fijo','Termino Fijo'),
            ('Indefinido', 'Indefinido'),
            ('Prestacion de Servicios', 'Prestacion de Servicios'),
            ('aprendizaje', 'aprendizaje')
        ]
    )
    Horario_laboral = models.CharField(max_length=200)
    Horas_Laborales = models.CharField(
        max_length=23,choices=[
            ('4-8 Horas','4-8 Horas'),
            ('9-16 Horas', '9-16 Horas'),
            ('17-25 Horas', '17-25 Horas'),
            ('26-35 Horas', '26-35 Horas'),
            ('36-45 Horas', '36-45 Horas'),
            ('46-55 Horas', '46-55 Horas'),
        ]
    )
    Promedio_Ingresos = models.CharField(
        max_length=23,choices=[
            ('0.5-1 SMLV ','0.5-1 SMLV '),
            ('1 SMLV ($1.160.000)', '1 SMLV ($1.160.000)'),
            ('Entre 1-2 SMLV ', 'Entre 1-2 SMLV '),
            ('Entre 1-3 SMLV ', 'Entre 1-3 SMLV '),
            ('Entre 1-4 SMLV ', 'Entre 1-4 SMLV '),
            ('Entre 1-5 SMLV ', 'Entre 1-5 SMLV '),
            ('Entre 1-6 SMLV ', 'Entre 1-6 SMLV '),
            ('Mas de 6 SMLV ', 'Mas de 6 SMLV '),
        ]
    )
    Frecuencia_Actividad_Fisica = models.CharField(
        max_length=22,choices=[
            ('1 vez por semana','1 vez por semana'),
            ('2 vez por semana', '2 vez por semana'),
            ('3 o mas vez por semana', '3 o mas vez por semana'),
            ('1 o 2 veces al mes', '1 o 2 veces al mes'),
            ('Todos los dias', 'Todos los dias'),
            ('Ninguna', 'Ninguna'),
        ]
    )
    Patologia_Mental = models.CharField(
        max_length=2,choices=[
            ('Si','Si'),
            ('No', 'No'),
        ]
    )
    Pareja_Embarazo = models.CharField(
        max_length=2,choices=[
            ('Si','Si'),
            ('No', 'No'),
        ]
    )
    PesoKg = models.FloatField()
    AlturaCm = models.FloatField()
    
    @property
    def IMC_Calculado(self):
        return self.PesoKg / (self.AlturaCm / 100) ** 2
    
    CATEGORIAS_OMS = [
        ('Delgadez Severa', 'Delgadez Severa'),
        ('Delgadez Moderada', 'Delgadez Moderada'),
        ('Delgadez Aceptable', 'Delgadez Aceptable'),
        ('Normal', 'Normal'),
        ('Sobrepeso', 'Sobrepeso'),
        ('Obesidad Tipo I', 'Obesidad Tipo I'),
        ('Obesidad Tipo II', 'Obesidad Tipo II'),
        ('Obesidad Tipo III', 'Obesidad Tipo III'),
    ]
    
    CategoriaSegunOMS = models.CharField(
        max_length=50,
        choices=CATEGORIAS_OMS,
        
    )
    Actualemte_Fuma = models.CharField(
        max_length=14,choices=[
            ('Diariamente','Diariamente'),
            ('Semanalmente','Semanalmente'),
            ('Quincenalmente','Quincenalmente'),
            ('Mensualmente','Mensualmente'),
            ('Ocasionalmente','Ocasionalmente'),
            ('Nunca', 'Nunca'),
        ]
    )
    Promedio_Cigarrillos = models.CharField(
        max_length=14,choices=[
            ('1-3','1-3'),
            ('4-6','4-6'),
            ('7-9','7-9'),
            ('9-11','9-11'),
            ('Mas de 12','Mas de 12'),
        ]
    )
    Consumo_Bebidas = models.CharField(
        max_length=14,choices=[
            ('Diariamente','Diariamente'),
            ('Semanalmente','Semanalmente'),
            ('Quincenalmente','Quincenalmente'),
            ('Mensualmente','Mensualmente'),
            ('Ocasionalmente','Ocasionalmente'),
            ('Nunca', 'Nunca'),
        ]
    )
    Frecuencia_Deporte = models.CharField(
        max_length=22,choices=[
            ('Diariamente','Diariamente'),
            ('1 vez por semana','1 vez por semana'),
            ('1-2 veces por semana', '1-2 veces por semana'),
            ('3-4 veces por semana ', '3-4 veces por semana '),
            ('5-6 veces por semana', '5-9 veces por semana'),
            ('Ocasionalmente','Ocasionalmente'),
        ]
    )
    Actualimente_Utiliza_Voz = models.CharField(
        max_length=2,choices=[
            ('Si','Si'),
            ('No', 'No'),
        ]
    )
    Horas_Utilizacion_Voz = models.CharField(
        max_length=14,choices=[
            ('0-4 Horas','0-4 Horas'),
            ('1-6 Horas','1-6 Horas'),
            ('1-8 Horas','1-8 Horas'),
            ('Mas de 8 Horas','Mas de 8 Horas'),
        ]
    )
    Utiliza_Manos_Libres = models.CharField(
        max_length=2,choices=[
            ('Si','Si'),
            ('No', 'No'),
        ]
    )
    Horas_Utilizacion_Manos_Libre = models.CharField(
        max_length=14,choices=[
            ('0-4 Horas','0-4 Horas'),
            ('1-6 Horas','1-6 Horas'),
            ('1-8 Horas','1-8 Horas'),
            ('Mas de 8 Horas','Mas de 8 Horas'),
        ]
    )
    file = models.FileField(validators=[validate_image_file_extension])
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        db_table = "Formulario_Sociodemografico"
class aseguramientoForm(models.Model):
    id_aseguramiento = models.AutoField(primary_key=True)
    medicina_prepagada = models.BooleanField(default=False)
    plan_complementario_salud = models.BooleanField(default=False)
    seguro_de_vida = models.BooleanField(default=False)
    seguro_exequial = models.BooleanField(default=False)
    emergencia_medica = models.BooleanField(default=False)
    previser = models.BooleanField(default=False)
    ninguna = models.BooleanField(default=False)
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        db_table = "Formulario_aseguramiento"
class familiarForm(models.Model):
    id_Familiar = models.AutoField(primary_key=True)
    Parentesco_Familiar = models.CharField(max_length=50, choices=[
        ('Pareja', 'Pareja'),
        ('Abuelos', 'Abuelos'),
        ('Otro Familiar', 'Otro Familiar'),
        ('Ciudador(a)', 'Ciudador(a)'),
        ('Guardería', 'Guardería'),
        ('No Requiere', 'No Requiere'),
        ('No Tengo Hijos', 'No Tengo Hijos'),
    ])
    Nombres_Familiar = models.CharField(max_length=20)
    Apellidos_Familiar = models.CharField(max_length=20)
    Fecha_Nacimiento_Familiar = models.DateField(default=timezone.now)
    Convivencia_Hijo = models.CharField(
        max_length=14,choices=[
            ('Si','Si'),
            ('No', 'No'),
            ('No Tengo Hijos', 'No Tengo Hijos'),
        ]
    )
    Requiere_Lugar_Para_Llevar_hijo = models.CharField(
        max_length=14,choices=[
            ('Si','Si'),
            ('No', 'No'),
            ('No Tengo Hijos', 'No Tengo Hijos'),
        ]
    )
    Sexo_Familiar = models.CharField(
        max_length=15,choices=[
            ('Masculino','Masculino'),
            ('Femenino', 'Femenino')
        ]
    )
    Dependiente_Economico = models.CharField(
        max_length=2,choices=[
            ('Si','Si'),
            ('No', 'No'),
        ]
    )
    Dependiente_Economico = models.CharField(
        max_length=2,choices=[
            ('Si','Si'),
            ('No', 'No'),
        ]
    )
   
    
    
    
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "Formulario_FamiliaresConvivencia"
class familiardiscapacidadForm(models.Model):
    id_familiardiscapacidadForm = models.AutoField(primary_key=True)
    padre = models.BooleanField(default=False)
    madre = models.BooleanField(default=False)
    hijo = models.BooleanField(default=False)
    hija = models.BooleanField(default=False)
    abuelo = models.BooleanField(default=False)
    abuela = models.BooleanField(default=False)
    nieto = models.BooleanField(default=False)
    nieta = models.BooleanField(default=False)
    hermano = models.BooleanField(default=False)
    hermana = models.BooleanField(default=False)
    tio = models.BooleanField(default=False)
    tia = models.BooleanField(default=False)
    primo = models.BooleanField(default=False)
    prima = models.BooleanField(default=False)
    sobrino = models.BooleanField(default=False)
    sobrina = models.BooleanField(default=False)
    cuñado = models.BooleanField(default=False)
    cuñada = models.BooleanField(default=False)
    suegro = models.BooleanField(default=False)
    suegra = models.BooleanField(default=False)
    yerno = models.BooleanField(default=False)
    nuera = models.BooleanField(default=False)
    esposo = models.BooleanField(default=False)
    esposa = models.BooleanField(default=False)
    Ninguno = models.BooleanField(default=False)
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "Formulario_Familiar_Discapacidad"       
class situacionesafectableForm(models.Model):
    id_situacionesafectable = models.AutoField(primary_key=True)
    Problemas_de_conducta = models.BooleanField(default=False)
    Problemas_de_pareja = models.BooleanField(default=False)
    Problemas_intrafamiliares = models.BooleanField(default=False)
    Dificultad_para_acceder_a_educación = models.BooleanField(default=False)
    Deudas_que_superan_los_ingresos = models.BooleanField(default=False)
    Enfermedad_de_algún_familiar = models.BooleanField(default=False)
    Desempleo = models.BooleanField(default=False)
    Muerte_reciente_de_personas_cercanas = models.BooleanField(default=False)
    Consumo_de_sustancias_psicoactivas = models.BooleanField(default=False)
    Muerte_reciente_de_mascotas = models.BooleanField(default=False)
    Ninguna_situacion_afectable = models.BooleanField(default=False)
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "Formulario_Situaciones_Afectables_Familiares"             
class mascotasForm(models.Model):
    id_mascota = models.AutoField(primary_key=True)
    Tipo_Mascota = models.CharField(
        max_length=30, choices=[
            ('perro', 'perro'),
            ('gato', 'gato'),
            ('pájaro', 'pájaro'),
            ('conejo', 'conejo'),
            ('hámster', 'hámster'),
            ('pez', 'pez'),
            ('tortuga', 'tortuga'),
            ('iguana', 'iguana'),
            ('serpiente', 'serpiente'),
            ('loro', 'loro'),
            ('canario', 'canario'),
            ('caballo', 'caballo'),
            ('cerdo', 'cerdo'),
            ('oveja', 'oveja'),
            ('cabra', 'cabra'),
            ('tarantula', 'tarantula'),
            ('Mini Pig', 'Mini Pig'),
            ('Ninguno', 'Ninguno'),
    ])
    Nombre_Mascota = models.CharField(max_length=20, blank=True, null=True)
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "Formulario_Mascotas"   
class transorteForm(models.Model):
    id_transporte = models.AutoField(primary_key=True)
    Caminando = models.BooleanField(default=False)
    Bicicleta = models.BooleanField(default=False)
    Moto = models.BooleanField(default=False)
    Carro = models.BooleanField(default=False)
    Comparto_Vehiculo = models.BooleanField(default=False)
    Transporte_Publico= models.BooleanField(default=False)
    Taxi = models.BooleanField(default=False)
    Plataforma_movilidad_Uber_Didi = models.BooleanField(default=False)
    Patineta = models.BooleanField(default=False)
    Modalidad_Virtual = models.BooleanField(default=False)
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "Formulario_Transporte"
    #  # lastname = models.CharField(max_length=50)
    # # email = models.EmailField(max_length=254)
    # # fecha_creacion = models.DateTimeField(default=timezone.now)
class recursosdigitales(models.Model):
    id_recursodigital = models.AutoField(primary_key=True)
    Microsoft_OneDrive_Google_Drive = models.BooleanField(default=False)
    Microsoft_o_Google_Calendar = models.BooleanField(default=False)
    Sharepoint = models.BooleanField(default=False)
    Microsoft_Sway = models.BooleanField(default=False)
    Microsoft_Forms = models.BooleanField(default=False)
    Microsoft_PowerBI = models.BooleanField(default=False)
    Microsoft_Excel = models.BooleanField(default=False)
    Microsoft_Planner = models.BooleanField(default=False)
    Microsoft_Power_Automate = models.BooleanField(default=False)
    Microsoft_Project = models.BooleanField(default=False)
    Microsoft_Teams = models.BooleanField(default=False)
    Microsoft_Yammer = models.BooleanField(default=False)   
    Kahoot = models.BooleanField(default=False)
    Google_Formularios = models.BooleanField(default=False)
    Google_Jamboard = models.BooleanField(default=False)
    Slack = models.BooleanField(default=False)
    Google_Padlet = models.BooleanField(default=False)
    Google_Meet = models.BooleanField(default=False)
    Google_Classroom = models.BooleanField(default=False)
    Google_Drawing = models.BooleanField(default=False)
    Google_Sites = models.BooleanField(default=False)
    Google_Blogger = models.BooleanField(default=False)
    Google_Earth = models.BooleanField(default=False)
    Google_Collections = models.BooleanField(default=False)
    Google_Currents = models.BooleanField(default=False)
    Google_Docs = models.BooleanField(default=False)
    Google_Sheets = models.BooleanField(default=False)
    Google_Slides = models.BooleanField(default=False)
    Google_Expeditions = models.BooleanField(default=False)
    Asana = models.BooleanField(default=False)
    Trello = models.BooleanField(default=False)
    VPN = models.BooleanField(default=False)
    Camscanner = models.BooleanField(default=False)
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "Formulario_RecursosDigitales"
class appaprendizajeForm(models.Model):
    id_recursodigital = models.AutoField(primary_key=True)
    Microsoft_OneDrive_Google_Drive = models.BooleanField(default=False)
    Microsoft_o_Google_Calendar = models.BooleanField(default=False)
    Sharepoint = models.BooleanField(default=False)
    Microsoft_Sway = models.BooleanField(default=False)
    Microsoft_Forms = models.BooleanField(default=False)
    Microsoft_PowerBI = models.BooleanField(default=False)
    Microsoft_Excel = models.BooleanField(default=False)
    Microsoft_Planner = models.BooleanField(default=False)
    Microsoft_Power_Automate = models.BooleanField(default=False)
    Microsoft_Project = models.BooleanField(default=False)
    Microsoft_Teams = models.BooleanField(default=False)
    Microsoft_Yammer = models.BooleanField(default=False)   
    Kahoot = models.BooleanField(default=False)
    Google_Formularios = models.BooleanField(default=False)
    Google_Jamboard = models.BooleanField(default=False)
    Slack = models.BooleanField(default=False)
    Google_Padlet = models.BooleanField(default=False)
    Google_Meet = models.BooleanField(default=False)
    Google_Classroom = models.BooleanField(default=False)
    Google_Drawing = models.BooleanField(default=False)
    Google_Sites = models.BooleanField(default=False)
    Google_Blogger = models.BooleanField(default=False)
    Google_Earth = models.BooleanField(default=False)
    Google_Collections = models.BooleanField(default=False)
    Google_Currents = models.BooleanField(default=False)
    Google_Docs = models.BooleanField(default=False)
    Google_Sheets = models.BooleanField(default=False)
    Google_Slides = models.BooleanField(default=False)
    Google_Expeditions = models.BooleanField(default=False)
    Asana = models.BooleanField(default=False)
    Trello = models.BooleanField(default=False)
    VPN = models.BooleanField(default=False)
    Camscanner = models.BooleanField(default=False)
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "Formulario_APP_Aprendizaje"       
class ofrecimientoForm(models.Model):
    id_ofrecimiento = models.AutoField(primary_key=True)     
    reconocimiento = models.BooleanField(default=False)
    compensacion_economica = models.BooleanField(default=False)
    actividades_de_voluntariado = models.BooleanField(default=False)
    actividades_deportivas_recreacionales = models.BooleanField(default=False)
    actividades_artisticas_culturales = models.BooleanField(default=False)
    convenios_acceder_cursos_programas = models.BooleanField(default=False)
    actividades_integracion_familiar = models.BooleanField(default=False)
    patrocinios_educativos = models.BooleanField(default=False)
    programas_situaciones_familiares = models.BooleanField(default=False)
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'Formulario_Ofrecimientos'
class desarrollopersonalForm(models.Model):
    id_desarrollopersonal = models.AutoField(primary_key=True)     
    Salud_financiera = models.BooleanField(default=False)
    Relaciones_familiares = models.BooleanField(default=False)
    Manejo_de_conflictos = models.BooleanField(default=False)
    Manejo_de_adicciones = models.BooleanField(default=False)
    Manejo_del_duelo = models.BooleanField(default=False)
    Estilos_de_vida_saludable = models.BooleanField(default=False)
    Salud_mental = models.BooleanField(default=False)
    Cuidado_parental = models.BooleanField(default=False)
    Enfermedades_crónicas = models.BooleanField(default=False)
    Enfermedades_de_transmisión_sexual = models.BooleanField(default=False)
    Prevención_y_manejo_del_cáncer = models.BooleanField(default=False)
    Expresión_oral_y_corporal = models.BooleanField(default=False)
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'Formulario_Desarrollo_Personal'        
class reconocimientoempresarialForm(models.Model):
    id_reconocimientoempresarial = models.AutoField(primary_key=True)     
    Participar_en_iniciativas_o_proyectos = models.BooleanField(default=False)
    Viajes = models.BooleanField(default=False)
    Bonos_en_dinero = models.BooleanField(default=False)
    Flexibilidad_horaria = models.BooleanField(default=False)
    Tiempo_libre = models.BooleanField(default=False)
    Patrocinios_para_formación_profesional = models.BooleanField(default=False)
    Patrocinios_para_desarrollo_personal = models.BooleanField(default=False)
    Bonos_actividades_recreación = models.BooleanField(default=False)
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'Formulario_Reconocimiento_Empresarial'
class actividadesculturalesForm(models.Model):
    id_actividadesculturales = models.AutoField(primary_key=True)     
    Conciertos = models.BooleanField(default=False)
    Exposiciones = models.BooleanField(default=False)
    Teatro = models.BooleanField(default=False)
    Cine = models.BooleanField(default=False)
    Leer_club_de_lectura = models.BooleanField(default=False)
    Bailar = models.BooleanField(default=False)
    Ver_televisión = models.BooleanField(default=False)
    Viajar = models.BooleanField(default=False)
    Pintar = models.BooleanField(default=False)
    Mandalas = models.BooleanField(default=False)
    Escritura = models.BooleanField(default=False)
    Bordado = models.BooleanField(default=False)
    Gastronomía = models.BooleanField(default=False)
    Canto = models.BooleanField(default=False)
    Escultura = models.BooleanField(default=False)
    Fotografía = models.BooleanField(default=False)
    Cerámica = models.BooleanField(default=False)
    Interpretación_musical = models.BooleanField(default=False)
    Ninguna = models.BooleanField(default=False)
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'Formulario_actividades_culturales'
class actividadessaludForm(models.Model):  
    id_actividadessalud = models.AutoField(primary_key=True)     
    Examen_de_laboratorio = models.BooleanField(default=False)
    Examen_medico_anual = models.BooleanField(default=False)
    Valoracion_osteomuscular = models.BooleanField(default=False)
    Tamizaje_vocal = models.BooleanField(default=False)
    Actividades_para_el_manejo_de_estres = models.BooleanField(default=False)
    Inspeccion_de_puesto_de_trabajo = models.BooleanField(default=False)
    Examen_Post_incapacidad = models.BooleanField(default=False)
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'Formulario_actividades_salud'
class tiempolibreForm(models.Model):
    id_tiempolibre = models.AutoField(primary_key=True)     
    Otro_trabajo = models.BooleanField(default=False)
    Labores_domesticas = models.BooleanField(default=False)
    Recreacion_y_deporte = models.BooleanField(default=False)
    Estudio = models.BooleanField(default=False)
    Ninguna = models.BooleanField(default=False)
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'Formulario_tiempo_libre'
class enfermedadesForm(models.Model):
    id_enfermedad = models.AutoField(primary_key=True)     
    Hipertension = models.BooleanField(default=False)
    Diabetes = models.BooleanField(default=False)
    Insuficiencia_cardiaca = models.BooleanField(default=False)
    Infarto_del_miocardio = models.BooleanField(default=False)
    Cardiopatia_congenita = models.BooleanField(default=False)
    Hipertension_pulmonar = models.BooleanField(default=False)
    Accidente_cerebro_vascular = models.BooleanField(default=False)
    Transplante_de_medula_u_otros_organos = models.BooleanField(default=False)
    Enfermedades_autoinmunes = models.BooleanField(default=False)
    VIH_SIDA = models.BooleanField(default=False)
    Cancer_en_los_ultimos_5_anos = models.BooleanField(default=False)
    Enfermedades_tratamiento_corticoesteroides = models.BooleanField(default=False)
    EPOC = models.BooleanField(default=False)
    Enfisema = models.BooleanField(default=False)
    Bronquitis_cronica = models.BooleanField(default=False)
    Fibrosis_pulmonar = models.BooleanField(default=False)
    Silicosis = models.BooleanField(default=False)
    Antracosis = models.BooleanField(default=False)
    Asma = models.BooleanField(default=False)
    Insuficiencia_renal = models.BooleanField(default=False)
    Cirrosis = models.BooleanField(default=False)
    Enfermedad_hepatica = models.BooleanField(default=False)
    Ninguna = models.BooleanField(default=False)
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'Formulario_Enfermedades'     
class deporteForm(models.Model):
    id_Deporte = models.AutoField(primary_key=True)     
    Ciclismo = models.BooleanField(default=False)
    Atletismo = models.BooleanField(default=False)
    Fútbol = models.BooleanField(default=False)
    Baloncesto = models.BooleanField(default=False)
    Voleyball = models.BooleanField(default=False)
    Tenis = models.BooleanField(default=False)
    Caminar = models.BooleanField(default=False)
    Gimnasio = models.BooleanField(default=False)
    Trotar = models.BooleanField(default=False)
    Yoga = models.BooleanField(default=False)
    Artes_Marciales = models.BooleanField(default=False)
    Natacion = models.BooleanField(default=False)
    Zumba = models.BooleanField(default=False)
    Crossfit = models.BooleanField(default=False)
    Ninguno = models.BooleanField(default=False)
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'Formulario_Deporte'
class molestaseismesesForm(models.Model):
    id_Molestias = models.AutoField(primary_key=True)     
    Dolor_de_cabeza = models.BooleanField(default=False)
    Dolor_de_cuello_espalda_y_cintura = models.BooleanField(default=False)
    Dolores_musculares = models.BooleanField(default=False)
    Dificultad_para_algun_movimiento = models.BooleanField(default=False)
    Tos_frecuente = models.BooleanField(default=False)
    Dificultad_respiratoria = models.BooleanField(default=False)
    Gastritis_ulcera = models.BooleanField(default=False)
    Otras_alteraciones_del_funcionamiento_digestivo = models.BooleanField(default=False)
    Alteraciones_del_sueño = models.BooleanField(default=False)
    Dificultad_para_concentrarse = models.BooleanField(default=False)
    Mal_genio = models.BooleanField(default=False)
    Nerviosismo = models.BooleanField(default=False)
    Cansancio_mental = models.BooleanField(default=False)
    Palpitaciones = models.BooleanField(default=False)
    Dolor_en_el_pecho = models.BooleanField(default=False)
    Cambios_visuales = models.BooleanField(default=False)
    Cansancio_fatiga_o_discomfort_visual = models.BooleanField(default=False)
    Pitos_o_ruidos_continuos_o_intermitentes_en_los_oidos = models.BooleanField(default=False)
    Dificultad_para_oir = models.BooleanField(default=False)
    Sensacion_permanente_de_cansancio = models.BooleanField(default=False)
    Alteraciones_en_la_piel = models.BooleanField(default=False)
    Ninguna = models.BooleanField(default=False)
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'Formulario_Molestias_seis_meses'       
class molestiasvozForm(models.Model):
    id_molestiasvoz = models.AutoField(primary_key=True)     
    Fatiga_Cansansio_vocal = models.BooleanField(default=False)
    Carraspeo_frecuente = models.BooleanField(default=False)
    Sensacion_de_cuerpo_extraño = models.BooleanField(default=False)
    Diafonia = models.BooleanField(default=False)
    Afonia = models.BooleanField(default=False)
    Ninguno = models.BooleanField(default=False)
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'Formulario_Molestias_Voz'
class sintomasaudicionForm(models.Model):
    id_sintomasaudicion = models.AutoField(primary_key=True)     
    Cansancio_o_fatiga_auditiva = models.BooleanField(default=False)
    Tinitus_pitos_zumbidos = models.BooleanField(default=False)
    Dolor_de_cabeza_frecuente = models.BooleanField(default=False)
    Sensacion_de_perdida_auditiva = models.BooleanField(default=False)
    Requiere_cada_vez_mas_volumen_en_sus_dispositivos = models.BooleanField(default=False)
    Ninguna = models.BooleanField(default=False)
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'Formulario_Sintomas_Audicion'
class contratacionForm(models.Model):
    id_Contrato = models.AutoField(primary_key=True)
    Tipo_Contrato = models.CharField(
        max_length=23,choices=[
            ('Termino Fijo','Termino Fijo'),
            ('Indefinido', 'Indefinido'),
            ('Prestacion de Servicios', 'Prestacion de Servicios'),
            ('aprendizaje', 'aprendizaje')
        ]
    )
    Cargo_Contrato = models.CharField(
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
    Fecha_Inicio_Contrato = models.DateField(default=timezone.now)
    Fecha_Fin_Contrato = models.DateField(default=timezone.now)
    Ingreso_Mensaul = models.FloatField()
    INgreso_Mensual_Escrito = models.CharField(max_length=100)
    Fecha_Peticion_Carta = models.DateField(default=timezone.now)
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        db_table = 'Formulario_Contratacion'
    
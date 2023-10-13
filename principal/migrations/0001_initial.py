# Generated by Django 4.2.6 on 2023-10-13 13:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import principal.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FormularioForm',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Documento', models.PositiveIntegerField()),
                ('Tipo_Documento', models.CharField(choices=[(' Cédula de Ciudadanía', 'Cédula de Ciudadanía'), (' Cédula de Extranjería', 'Cédula de Extranjería'), (' Tarjeta de Identidad', 'Tarjeta de Identidad'), (' Pasaporte', 'Pasaporte'), (' Registro Civil', 'Registro Civil')], max_length=30)),
                ('tipo_sangre', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=3)),
                ('Cargo_Actual', models.CharField(choices=[('Academic Advisor', 'Academic Advisor'), ('Analista Contable', 'Analista Contable'), ('Analista de compensación', 'Analista de compensación'), ('Analista de comunicaciones', 'Analista de comunicaciones'), ('Analista de Gestión Organizacional', 'Analista de Gestión Organizacional'), ('Asesor Servicios Integrales', 'Asesor Servicios Integrales'), ('Asesora EduSA', 'Asesora EduSA'), ('Asistente Académico', 'Asistente Académico'), ('Asistente Cultural', 'Asistente Cultural'), ('Asistente de Comunicaciones', 'Asistente de Comunicaciones'), ('Asistente de Dirección', 'Asistente de Dirección'), ('Asistente de Innovación y Negocios', 'Asistente de Innovación y Negocios'), ('Asistente de Recursos Administrativos', 'Asistente de Recursos Administrativos'), ('Asistente de servicios bibliotecarios', 'Asistente de servicios bibliotecarios'), ('Asistente Maker', 'Asistente Maker'), ('Aprendiz', 'Aprendiz'), ('Auxiliar Contable', 'Auxiliar Contable'), ('Auxiliar de mantenimiento y recursos físicos', 'Auxiliar de mantenimiento y recursos físicos'), ('Auxiliar de Selección y contratación', 'Auxiliar de Selección y contratación'), ('Auxiliar de seguridad', 'Auxiliar de seguridad'), ('Auxiliar de Soporte Técnico', 'Auxiliar de Soporte Técnico'), ('Auxiliar Tecnología Educativa', 'Auxiliar Tecnología Educativa'), ('Coordinador académico sede sur', 'Coordinador académico sede sur'), ('Coordinador de acompañamiento psicosocial', 'Coordinador de acompañamiento psicosocial'), ('Coordinador de mercadeo', 'Coordinador de mercadeo'), ('Coordinador de proyectos especiales', 'Coordinador de proyectos especiales'), ('Coordinador de Programación y Gestión Comercial', 'Coordinador de Programación y Gestión Comercial'), ('Coordinador de servicios STEAM y bibliotecas', 'Coordinador de servicios STEAM y bibliotecas'), ('Coordinador sede virtual', 'Coordinador sede virtual'), ('Coordinadora de programa Kids and Teens', 'Coordinadora de programa Kids and Teens'), ('Coordinadora de responsabilidad social y egresados', 'Coordinadora de responsabilidad social y egresados'), ('Coordinadora sede norte', 'Coordinadora sede norte'), ('Desarrollador de producto', 'Desarrollador de producto'), ('Director Cultural', 'Director Cultural'), ('Director de Innovación y negocios', 'Director de Innovación y negocios'), ('Director Financiero y Administrativo', 'Director Financiero y Administrativo'), ('Director General', 'Director General'), ('Docente', 'Docente'), ('Jefe de Comunicaciones', 'Jefe de Comunicaciones'), ('Jefe de Contabilidad', 'Jefe de Contabilidad'), ('Jefe de Desarrollo de Producto', 'Jefe de Desarrollo de Producto'), ('Jefe de Gestión Humana', 'Jefe de Gestión Humana'), ('Jefe de Gestión Organizacional', 'Jefe de Gestión Organizacional'), ('Jefe de mantenimiento y recursos físicos', 'Jefe de mantenimiento y recursos físicos'), ('Jefe de Servicios Culturales', 'Jefe de Servicios Culturales'), ('Jefe de Servicios Integrales', 'Jefe de Servicios Integrales'), ('Recepcionista', 'Recepcionista'), ('Subdirector académico', 'Subdirector académico'), ('Support Teacher', 'Support Teacher'), ('Técnico electricista', 'Técnico electricista'), ('Técnico electrónico', 'Técnico electrónico'), ('Conductor-mensajero', 'Conductor-mensajero')], max_length=100)),
                ('Numero_Contacto', models.PositiveIntegerField()),
                ('Numero_Emergencia', models.PositiveIntegerField()),
                ('Fecha_Nacimiento', models.DateTimeField(default=django.utils.timezone.now)),
                ('Departamento_Nacimiento', models.CharField(max_length=20, validators=[principal.models.contiene_mayuscula])),
                ('Ciudad_Nacimiento', models.CharField(max_length=20, validators=[principal.models.contiene_mayuscula])),
                ('Ciudad_Residencia', models.CharField(max_length=20, validators=[principal.models.contiene_mayuscula])),
                ('Direccion_Residencia', models.CharField(max_length=100)),
                ('Sexo', models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=15)),
                ('Estado_Civil', models.CharField(choices=[('Soltero(a)', 'Soltero(a)'), ('Casado(a)', 'Casado(a)'), ('Union Libre', 'Union Libre'), ('Viudo(a)', 'Viudo(a)')], max_length=15)),
                ('Etnia', models.CharField(choices=[('Mestizo', 'Mestizo'), ('Afrocolombiano', 'Afrocolombiano'), ('Indígena', 'Indígena'), ('Blanco', 'Blanco'), ('Meztizo', 'Meztizo'), ('Mulato', 'Mulato'), ('Zambo', 'Zambo'), ('Raizal', 'Raizal')], max_length=15)),
                ('Talla_Camisa', models.CharField(choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'), ('XXXL', 'XXXL')], max_length=15)),
                ('Vegetariano', models.CharField(choices=[('Si', 'Si'), ('No', 'No')], max_length=2)),
                ('Actualmente_Tiene_Restricciones_Laborales_Por_Su_EPS', models.CharField(choices=[('Si', 'Si'), ('No', 'No')], max_length=2)),
                ('Actualmente_Se_Encuentra_En_Perdida_De_Capacidad_Laboral', models.CharField(choices=[('Si', 'Si'), ('No', 'No')], max_length=2)),
                ('Pensionado', models.CharField(choices=[('Por vejez', 'Por vejez'), ('Por invalidez', 'Por invalidez'), ('No', 'No')], max_length=13)),
                ('file', models.FileField(upload_to='', validators=[principal.models.validate_image_file_extension])),
                ('idUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Formulario',
            },
        ),
        migrations.CreateModel(
            name='aseguramientoForm',
            fields=[
                ('id_Aseguramiento', models.AutoField(primary_key=True, serialize=False)),
                ('Tipo_Aseguramiento', models.CharField(choices=[('Medicina prepagada', 'Medicina prepagada'), ('Plan complementario de salud', 'Plan complementario de salud'), ('Seguro de vida', 'Seguro de vida'), ('Seguro excequial', 'Seguro excequial'), ('Emergencia médica (Ej. Emi, CEM)', 'Emergencia médica (Ej. Emi, CEM)'), ('Previser', 'Previser'), ('Ninguna', 'Ninguna')], max_length=50)),
                ('idUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'aseguramiento_aseguramientoform',
            },
        ),
    ]

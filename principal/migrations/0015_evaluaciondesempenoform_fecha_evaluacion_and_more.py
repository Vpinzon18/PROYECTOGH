# Generated by Django 4.2.6 on 2023-11-15 15:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0014_alter_formularioform_tipo_sangre'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluaciondesempenoform',
            name='Fecha_Evaluacion',
            field=models.DateField(default=datetime.date(2023, 11, 15)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='formularioform',
            name='tipo_sangre',
            field=models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=3),
        ),
    ]

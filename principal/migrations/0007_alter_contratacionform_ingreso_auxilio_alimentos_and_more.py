# Generated by Django 4.2.6 on 2023-11-13 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0006_contratacionform_descripcion_carta_laboral'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contratacionform',
            name='Ingreso_Auxilio_Alimentos',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='contratacionform',
            name='Ingreso_Auxilio_monetario',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='contratacionform',
            name='Ingreso_Mensual_monetario',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
    ]
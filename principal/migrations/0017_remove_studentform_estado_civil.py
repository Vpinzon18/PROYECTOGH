# Generated by Django 3.2.21 on 2023-09-28 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0016_studentform_estado_civil'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentform',
            name='estado_civil',
        ),
    ]

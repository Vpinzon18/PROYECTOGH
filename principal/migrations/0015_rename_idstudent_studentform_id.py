# Generated by Django 3.2.21 on 2023-09-28 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0014_rename_id_studentform_idstudent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentform',
            old_name='idstudent',
            new_name='id',
        ),
    ]
# Generated by Django 3.2.21 on 2023-09-28 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0019_rename_numerodocumento_studentform_firstname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentform',
            old_name='firstname',
            new_name='Documento',
        ),
    ]
# Generated by Django 4.2 on 2023-05-02 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_perfil_autor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tags',
            new_name='categoria',
        ),
    ]

# Generated by Django 4.2.2 on 2023-06-13 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_servicio_usuariopersonalizado_delete_task_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuariopersonalizado',
            old_name='usuario',
            new_name='username',
        ),
        migrations.AddField(
            model_name='usuariopersonalizado',
            name='password',
            field=models.CharField(blank=True, max_length=15, unique=True),
        ),
    ]

# Generated by Django 3.2.11 on 2022-05-05 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_perfil_biografia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='biografia',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

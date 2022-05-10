# Generated by Django 3.2.11 on 2022-05-05 04:58

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_alter_perfil_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='avatar',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=-1, size=(300, 300), upload_to='pics/'),
        ),
    ]

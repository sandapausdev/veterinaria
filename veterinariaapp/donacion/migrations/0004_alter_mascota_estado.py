# Generated by Django 4.0.4 on 2022-05-05 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donacion', '0003_alter_mascota_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='estado',
            field=models.IntegerField(default=0),
        ),
    ]
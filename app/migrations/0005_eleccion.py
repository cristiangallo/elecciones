# Generated by Django 4.2.3 on 2023-07-04 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_candidato_foto_alter_partido_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eleccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.IntegerField(default=2023, verbose_name='Año')),
                ('tipo_eleccion', models.CharField(default='P', max_length=1)),
                ('fecha_comicios', models.DateField()),
            ],
        ),
    ]

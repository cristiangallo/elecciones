# Generated by Django 4.2.3 on 2023-07-04 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_cargoelecto_ult_actualizacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargoelecto',
            name='pais',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='app.country', verbose_name='País'),
            preserve_default=False,
        ),
    ]

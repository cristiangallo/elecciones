# Generated by Django 4.2.3 on 2023-07-04 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partido',
            name='logo',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='imagenes/logos/'),
        ),
    ]

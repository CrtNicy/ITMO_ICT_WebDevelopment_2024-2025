# Generated by Django 5.1.4 on 2024-12-07 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warriors_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skillofwarrior',
            name='level',
            field=models.IntegerField(default=1, verbose_name='Уровень освоения умения'),
        ),
    ]

# Generated by Django 5.1.4 on 2024-12-06 17:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marka', models.CharField(max_length=100, verbose_name='Марка')),
                ('model', models.CharField(max_length=100, verbose_name='Модель автомобиля')),
                ('color', models.CharField(max_length=50, verbose_name='Цвет автомобиля')),
            ],
        ),
        migrations.CreateModel(
            name='Avtovladelec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя владельца')),
            ],
        ),
        migrations.CreateModel(
            name='Udoverenie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_issued', models.DateField(verbose_name='Дата выдачи удостоверения')),
                ('avtovladelec', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='udoverenie', to='app_name.avtovladelec')),
            ],
        ),
        migrations.CreateModel(
            name='Vladenie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(verbose_name='Год владения')),
                ('avto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vladenie_avtovladelec', to='app_name.avto')),
                ('avtovladelec', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vladenie_avto', to='app_name.avtovladelec')),
            ],
        ),
    ]

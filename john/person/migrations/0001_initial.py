# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
            ],
        ),
        migrations.CreateModel(
            name='CityNeighborhood',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Nome')),
                ('city', models.ForeignKey(default=1, verbose_name=b'Cidade', to='person.City')),
            ],
        ),
        migrations.CreateModel(
            name='CityRegion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=50, verbose_name='Descri\xe7\xe3o')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150, verbose_name=b'Nome')),
                ('address', models.CharField(max_length=250, null=True, verbose_name='Endere\xe7o', blank=True)),
                ('zip_code', models.CharField(max_length=9, null=True, verbose_name=b'CEP', blank=True)),
                ('phone', models.CharField(max_length=14, null=True, verbose_name=b'Telefone', blank=True)),
                ('mobile_phone', models.CharField(max_length=16, null=True, verbose_name=b'Celular', blank=True)),
                ('birthdate', models.DateField(null=True, verbose_name='Data de anivers\xe1rio', blank=True)),
                ('sex', models.CharField(blank=True, max_length=1, null=True, verbose_name='Sexo', choices=[(b'M', b'Masculino'), (b'F', b'Feminino')])),
                ('cpf', models.CharField(max_length=14, null=True, verbose_name=b'CPF', blank=True)),
                ('city', models.ForeignKey(default=1, verbose_name=b'Cidade', to='person.City')),
                ('neighborhood', models.ForeignKey(verbose_name=b'Bairro', to='person.CityNeighborhood')),
            ],
        ),
        migrations.AddField(
            model_name='cityneighborhood',
            name='city_region',
            field=models.ForeignKey(verbose_name=b'Regi\xc3\xa3o', to='person.CityRegion'),
        ),
    ]

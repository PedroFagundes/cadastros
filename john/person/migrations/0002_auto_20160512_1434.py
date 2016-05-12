# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'Cidade', 'verbose_name_plural': 'Cidades'},
        ),
        migrations.AlterModelOptions(
            name='cityneighborhood',
            options={'verbose_name': 'Bairro', 'verbose_name_plural': 'Bairros'},
        ),
        migrations.AlterModelOptions(
            name='cityregion',
            options={'verbose_name': 'Regi\xe3o', 'verbose_name_plural': 'Regi\xf5es'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Pessoa', 'verbose_name_plural': 'Pessoas'},
        ),
        migrations.AddField(
            model_name='person',
            name='alternative_phone_1',
            field=models.CharField(max_length=16, null=True, verbose_name=b'Telefone alternativo 1', blank=True),
        ),
        migrations.AddField(
            model_name='person',
            name='alternative_phone_2',
            field=models.CharField(max_length=16, null=True, verbose_name=b'Telefone alternativo 2', blank=True),
        ),
        migrations.AddField(
            model_name='person',
            name='alternative_phone_3',
            field=models.CharField(max_length=16, null=True, verbose_name=b'Telefone alternativo 3', blank=True),
        ),
    ]

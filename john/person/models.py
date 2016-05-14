# -*- coding: utf-8 -*-
from django.db import models


class CityRegion(models.Model):
    description = models.CharField(u'Descrição', max_length=50, blank=False, null=False)

    class Meta:
        verbose_name = 'Região'
        verbose_name_plural = 'Regiões'

    def __unicode__(self):
        return unicode(self.description)


class City(models.Model):
    name = models.CharField(u'Nome', max_length=50, blank=False, null=False)

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'

    def __unicode__(self):
        return unicode(self.name)


class CityNeighborhood(models.Model):
    city = models.ForeignKey(City, verbose_name='Cidade', default=1)
    name = models.CharField('Nome', max_length=50, blank=False, null=False)
    city_region = models.ForeignKey(CityRegion, verbose_name='Região')

    class Meta:
        verbose_name = 'Bairro'
        verbose_name_plural = 'Bairros'

    def __unicode__(self):
        return unicode(self.name)


class Person(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    PERSON_SEX_CHOICES = (
        (MALE, 'Masculino'),
        (FEMALE, 'Feminino')
    )
    name = models.CharField('Nome', max_length=150, blank=False, null=False)
    address = models.CharField(u'Endereço', max_length=250, blank=True, null=True)
    city = models.ForeignKey(City, verbose_name='Cidade', default=1)
    neighborhood = models.ForeignKey(CityNeighborhood, verbose_name='Bairro', blank=False, null=False)
    zip_code = models.CharField('CEP', max_length=9, blank=True, null=True)
    phone = models.CharField('Telefone', max_length=14, blank=True, null=True)
    mobile_phone = models.CharField('Celular', max_length=16, blank=True, null=True)
    alternative_phone_1 = models.CharField('Telefone alternativo 1', max_length=16, blank=True, null=True)
    alternative_phone_2 = models.CharField('Telefone alternativo 2', max_length=16, blank=True, null=True)
    alternative_phone_3 = models.CharField('Telefone alternativo 3', max_length=16, blank=True, null=True)
    birthdate = models.CharField(u'Data de aniversário', max_length=10, blank=True, null=True)
    sex = models.CharField('Sexo', max_length=1, choices=PERSON_SEX_CHOICES, blank=True, null=True)
    cpf = models.CharField('CPF', max_length=14, blank=True, null=True)

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'

    def __unicode__(self):
        return unicode(self.name)

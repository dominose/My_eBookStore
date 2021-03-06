# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-27 12:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=30)),
                ('abstract', models.TextField()),
                ('price', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('solid', models.IntegerField()),
                ('classify', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=30)),
                ('orded_book', models.CharField(max_length=30)),
                ('number', models.IntegerField()),
                ('order_value', models.IntegerField()),
                ('time', models.DateTimeField()),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ShopCar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ShopCar_user', models.CharField(max_length=30)),
                ('Shops', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('tel', models.IntegerField()),
                ('address', models.CharField(max_length=50)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-10 02:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_choice', models.CharField(max_length=200)),
                ('calories', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='food',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nutritionCalculator.Food'),
        ),
    ]

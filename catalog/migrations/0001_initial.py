# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cat_num', models.CharField(max_length=255)),
                ('term', models.CharField(max_length=255)),
                ('bracketed', models.BooleanField(default=False)),
                ('field', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=255)),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('prerequisites', models.TextField()),
                ('notes', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('format', models.CharField(max_length=255)),
                ('building', models.CharField(max_length=255)),
                ('room', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first', models.CharField(max_length=255)),
                ('middle', models.CharField(max_length=255)),
                ('last', models.CharField(max_length=255)),
                ('suffix', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day', models.CharField(max_length=255)),
                ('format', models.CharField(max_length=255)),
                ('optional', models.BooleanField(default=False)),
                ('begin_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='course',
            name='faculty',
            field=models.ManyToManyField(to='catalog.Professor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='locations',
            field=models.ManyToManyField(to='catalog.Location'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='schedule',
            field=models.ForeignKey(to='catalog.Schedule'),
            preserve_default=True,
        ),
    ]

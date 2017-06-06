# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-06 17:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Demo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(default='', max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('version', models.DateField(blank=True, default=datetime.datetime(2017, 6, 6, 17, 46, 46, 386799))),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=50)),
                ('name', models.CharField(blank=True, default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PositionData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.CharField(blank=True, default='', max_length=300)),
                ('notes', models.TextField(blank=True, default='', max_length=1000)),
                ('demo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='position_player.Demo')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='position_player.Player')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='demo',
            name='context',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='position_player.Tournament'),
        ),
        migrations.AddField(
            model_name='demo',
            name='team1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team1', to='position_player.Team'),
        ),
        migrations.AddField(
            model_name='demo',
            name='team2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team2', to='position_player.Team'),
        ),
    ]

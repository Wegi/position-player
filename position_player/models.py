from django.db import models
import datetime


# Create your models here.
class Player(models.Model):
    nickname = models.CharField(blank=False, max_length=50)
    name = models.CharField(blank=True, default='', max_length=100)


class Map(models.Model):
    name = models.CharField(blank=False, max_length=50)
    version = models.DateField(blank=True, default=datetime.datetime.today())


class Team(models.Model):
    name = models.CharField(blank=False, max_length=50)


class Tournament(models.Model):
    name = models.CharField(blank=False, max_length=200)


class Demo(models.Model):
    team1 = models.ForeignKey(Team, related_name='team1')
    team2 = models.ForeignKey(Team, related_name='team2')
    context = models.ForeignKey(Tournament)
    source = models.CharField(blank=False, default='', max_length=400)


class PositionData(models.Model):
    demo = models.ForeignKey(Demo)
    player = models.ForeignKey(Player)
    timestamp = models.CharField(blank=True, default='', max_length=300)
    notes = models.TextField(blank=True, default='', max_length=1000)

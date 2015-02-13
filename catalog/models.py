import datetime
from django.db import models

# Create your models here.
class Professor(models.Model):
	first = models.CharField(max_length=255)
	middle = models.CharField(max_length=255)
	last = models.CharField(max_length=255)
	suffix = models.CharField(max_length=255)

class Schedule(models.Model):
	day = models.CharField(max_length=255)
	format = models.CharField(max_length=255)
	optional = models.BooleanField(default=False)
	begin_time = models.TimeField()
	end_time = models.TimeField()

class Location(models.Model):
	format = models.CharField(max_length=255)
	building = models.CharField(max_length=255)
	room = models.CharField(max_length=255)

class Course(models.Model):
	cat_num = models.CharField(max_length=255)
	term = models.CharField(max_length=255)
	bracketed = models.BooleanField(default=False)
	field = models.CharField(max_length=255)
	number = models.CharField(max_length=255)
	title = models.TextField()
	faculty = models.ManyToManyField(Professor)
	schedule = models.ForeignKey(Schedule)
	locations = models.ManyToManyField(Location)
	description = models.TextField()
	prerequisites = models.TextField()
	notes = models.TextField()
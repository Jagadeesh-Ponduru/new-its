from __future__ import unicode_literals

from django.db import models
import datetime

# Create your models here.

class Sensor(models.Model):#Stores information about sensor values
    Sensor_name  = models.CharField(max_length=200,default=None)
    Sensor_value = models.CharField(max_length=200,default=None)
    Sensor_date  = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '@'+self.Sensor_name


class Sensorgroup2(models.Model):#Stores information about sensor values
    Sensorgroup2_group  = models.CharField(max_length=200,default='group_two')
    Sensorgroup2_name  = models.CharField(max_length=200,default=None)

    Sensorgroup2_value = models.CharField(max_length=200,default=None)
    Sensorgroup2_date  = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '@'+self.Sensorgroup2_name

from django.db import models
import datetime
from orderapp.models import *

# Create your models here.
class Employee(models.Model):
    employeeid = models.ForeignKey(Person)
    order = models.ManyToManyField(Order)

    def __unicode__(self):
        return '%d' % (self.employeeid)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
        ordering = ['employeeid',]
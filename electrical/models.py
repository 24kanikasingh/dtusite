# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    qual = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    special = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.name

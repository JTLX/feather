# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Todo(models.Model):
    owner = models.ForeignKey(User)
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=10000)
    priority = models.IntegerField()
    due_date = models.DateTimeField('due date')
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class TodoList(models.Model):
    owner = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    color = models.CharField(max_length=20, default="#000000")

    def __unicode__(self):
        return self.title

class Todo(models.Model):
    owner = models.ForeignKey(User)
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=10000)
    priority = models.IntegerField()
    todo_list = models.ForeignKey(TodoList)
    due_date = models.DateTimeField('due date')
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')
    
    def __unicode__(self):
        return self.title

class TodoTag(models.Model):
    owner = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    color = models.CharField(max_length=20, default="#000000")
    todos = models.ManyToManyField(Todo)

    def __unicode__(self):
        return self.title

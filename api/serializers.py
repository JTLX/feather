from django.contrib.auth.models import User, Group
from todo.models import Todo
from rest_framework import serializers


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('owner', 'title', 'description', 'priority', 'todo_list', 'due_date', 'start_date', 'end_date')


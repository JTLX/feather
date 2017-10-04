from django.contrib.auth.models import User, Group
from todo.models import Todo
from rest_framework import viewsets
from serializers import TodoSerializer

import sys

print (sys.path)
class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Todo.objects.all().order_by('-due_date')
    serializer_class = TodoSerializer

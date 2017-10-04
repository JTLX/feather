from django.contrib.auth.models import User, Group
from todo.models import Todo
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from serializers import TodoSerializer


class TodoViewSet(viewsets.ViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = Todo.objects.filter(owner=request.user).order_by('-due_date')
        serializer = TodoSerializer(queryset, many=True)
        return Response(serializer.data)

from .serializers import TodoSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Todo


class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

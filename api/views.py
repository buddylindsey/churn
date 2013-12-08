#from django.http import Http404

#from rest_framework.views import APIView
#from rest_framework.response import Response
#from rest_framework import status
from rest_framework import generics

from task.models import Task
from .serializers import TaskSerializer


class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

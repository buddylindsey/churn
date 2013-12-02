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


#class TaskList(APIView):

    #def get(self, request, format=None):
        #tasks = Task.objects.all()
        #serializer = TaskSerializer(tasks, many=True)
        #return Response(serializer.data)

    #def post(self, request, format=None):
        #serializer = TaskSerializer(data=request.DATA)
        #if serializer.is_valid():
            #serializer.save()
            #return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#class TaskDetail(APIView):

    #def get_object(self, pk):
        #try:
            #return Task.objects.get(pk=pk)
        #except Task.DoesNotExist:
            #raise Http404

    #def get(self, request, pk, format=None):
        #task = self.get_object(pk)
        #serializer = TaskSerializer(task)
        #return Response(serializer.data)

    #def put(self, request, pk, format=None):
        #task = self.get_object(pk)
        #serializer = TaskSerializer(task, data=request.DATA)
        #if serializer.is_valid():
            #serializer.save()
            #return Response(serializer.data)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #def delete(self, request, pk, format=None):
        #task = self.get_object(pk)
        #task.delete()
        #return Response(status=status.HTTP_204_NO_CONTENT)

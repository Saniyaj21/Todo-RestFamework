from django.shortcuts import render

from django.http import JsonResponse
from .models import Task

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import TaskSerializers


# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    context = {'name': 'Saniyaj Mallik'}
    return Response (context)


@api_view(['GET'])
def taskList(request):

    tasks = Task.objects.all()
    serializer = TaskSerializers(tasks, many = True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request, pk):

    tasks = Task.objects.get(id = pk)
    serializer = TaskSerializers(tasks, many = False)
    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):

    
    serializer = TaskSerializers(data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def taskUpdate(request, pk):

    task = Task.objects.get(id = pk)
    
    serializer = TaskSerializers(instance = task, data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request, pk):

    task = Task.objects.get(id = pk)
    task.delete()
    return Response("Item Deleted")

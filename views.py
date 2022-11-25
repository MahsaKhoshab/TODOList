from django.http import JsonResponse
from rest_framework.decorators import api_view

from .models import ToDoList
from .serializers import TodolistSerializer

from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def todolist_list(request, format=None):
    if request.method == 'GET':
        # get all to do activities
        # serialize them
        # return json
        todolist = ToDoList.objects.all()
        serializer = TodolistSerializer(todolist, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        #take the data
        #deserialize
        #create a todolist object
        serializer = TodolistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def todolist_detail(request, id, format=None):
    try:
        todolist = ToDoList.objects.get(pk=id)
    except ToDoList.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TodolistSerializer(todolist)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TodolistSerializer(todolist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        todolist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# to see it on python , consumapi.py
# let the server running , and do
# import requests
# response = requests.get('http://127.0.0.1.8000/todolist')
# print(response.json())
from rest_framework import serializers
from .models import ToDoList


class TodolistSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = ['id', 'activity_name', 'description']


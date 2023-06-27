from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *


# Create your views here.


# for reading from ToDo list

class ListToDo(generics.ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class =ToDoSerializer

# for updating the ToDo list

class DetailToDo(generics.RetrieveUpdateAPIView):
    queryset = ToDo.objects.all()
    serializer_class =ToDoSerializer

# for creating the ToDo list

class CreateToDo(generics.CreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class =ToDoSerializer


# for deleting from ToDo list

class DeleteToDo(generics.DestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class =ToDoSerializer

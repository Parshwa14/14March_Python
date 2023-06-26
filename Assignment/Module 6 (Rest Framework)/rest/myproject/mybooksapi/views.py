from django.shortcuts import render
from .models import *
from .serializers import BookSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.

def book(request):
    b_all = Book.objects.all()
    serializer = BookSerializer(b_all,many = True)
    
    #serializer data convert into json format
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type = "application/json")
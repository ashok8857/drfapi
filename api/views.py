from django.db.models.query import QuerySet
from django.shortcuts import render

# Create your views here.
from .models import StuInfo
from .serializers import StuSerializers
from rest_framework import generics




class Createlist(generics.CreateAPIView):
    queryset=StuInfo.objects.all()
    serializer_class=StuSerializers    
    

class Showlist(generics.ListAPIView):
    queryset=StuInfo.objects.all()

    serializer_class=StuSerializers    


class Deleterec(generics.DestroyAPIView):
    queryset=StuInfo.objects.all()
    serializer_class=StuSerializers       
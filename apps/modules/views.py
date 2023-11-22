from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets

# Create your views here.

class ModuleViewSet(viewsets.ModelViewSet):
  queryset = Module.objects.all()
  serializer_class = ModuleSerializer
  
class GroupViewSet(viewsets.ModelViewSet):
  queryset = Group.objects.all()
  serializer_class = GroupSerializer

class GroupModulesViewSet(viewsets.ModelViewSet):
  queryset = GroupModules.objects.all()
  serializer_class = GroupModulesSerializer
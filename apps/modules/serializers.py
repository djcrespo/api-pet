from rest_framework import serializers
from .models import *

class ModuleSerializer(serializers.ModelSerializer):
  class Meta:
    model = Module
    fields = "__all__"

class GroupSerializer(serializers.ModelSerializer):
  class Meta:
    model = Group
    fields = "__all__"

class GroupModulesSerializer(serializers.ModelSerializer):
  class Meta:
    model = GroupModules
    fields = "__all__"
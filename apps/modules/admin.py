from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
  list_display = ['id', 'name', 'description']
  list_filter = ['name']
  list_per_page = 10

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
  list_display = ['id', 'name', 'description']
  list_filter = ['name']
  list_per_page = 10

@admin.register(GroupModules)
class GroupModulesAdmin(admin.ModelAdmin):
  list_display = ['group']
  list_filter = ['group']
  list_per_page = 10
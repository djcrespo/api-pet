from django.db import models

# Create your models here.
class Module(models.Model):
  id = models.BigAutoField(primary_key=True, editable=False, verbose_name='ID')
  name = models.CharField(max_length=100, null=False, verbose_name='Nombre')
  description = models.CharField(verbose_name="Descripción", max_length=255, null=True)
  is_active = models.BooleanField(verbose_name="Activo?", default=True, null=False)

  def __str__(self):
    return str(self.id)
  
class Group(models.Model):
  id = models.BigAutoField(verbose_name='ID', primary_key=True, editable=False)
  name = models.CharField(verbose_name='Nombre', max_length=100, null=False)
  description = models.CharField(verbose_name="Descripción", max_length=255, null=True)
  is_active = models.BooleanField(verbose_name="Activo?", default=True, null=False)

  def __str__(self):
    return str(self.id)

class GroupModules(models.Model):
  group = models.OneToOneField(Group, verbose_name='Grupo de módulos/sensores', on_delete=models.CASCADE, null=False)
  modules = models.ManyToManyField(Module, verbose_name='Módulos/Sensores')

  def __str__(self):
    return str(self.group.id)
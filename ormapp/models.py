# Create your models here.
from django.db import models
from django.contrib import admin
class football_players(models.Model):
  first_name=models.CharField(max_length=30)
  last_name=models.CharField(max_length=30)
  dob=models.DateField()
  age=models.IntegerField()
  matches_played=models.IntegerField()
  total_goals=models.IntegerField()
  email=models.EmailField()

class football_playersAdmin(admin.ModelAdmin):
  list_display=('first_name','last_name','dob','age','matches_played','total_goals','email')
from django.contrib import admin

# Register your models here.
from .models import football_players,football_playersAdmin
admin.site.register(football_players,football_playersAdmin)
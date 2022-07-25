from django.contrib import admin
from .models import Cars

@admin.register(Cars)
class CarsModelAdmin(admin.ModelAdmin):
 list_display = ['id', 'name', 'dom', 'type', 'locality', 'city', 'pin', 'state', 'mobile', 'manufacture_city', 'profile_image']
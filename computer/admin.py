from django.contrib import admin
from .models import Computer, ComputerBrand, ComputerGeneration

# Register your models here.
admin.site.register(ComputerBrand)
admin.site.register(Computer)
admin.site.register(ComputerGeneration)

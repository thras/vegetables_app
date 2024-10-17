from django.contrib import admin
from .models import Vegetable

# Register your models here.
class VegetableListAdmin(admin.ModelAdmin):
    list_display = ("name", "calorie", "kilojoule","category","photo")

admin.site.register(Vegetable, VegetableListAdmin)
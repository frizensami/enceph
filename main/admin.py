from django.contrib import admin
from main.models import Category, Tool

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Tool)
class TaskAdmin(admin.ModelAdmin):
    pass



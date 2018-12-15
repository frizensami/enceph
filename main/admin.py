from django.contrib import admin
from main.models import Category, Task

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass



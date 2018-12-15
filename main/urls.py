from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_tool', views.new_tool, name='new_tool'),
]
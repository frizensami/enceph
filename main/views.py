from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from main.models import Category, Tool

# Create your views here.
def index(request):
    template = loader.get_template('main/index.html')
    categories = Category.objects.all()
    tools = Tool.objects.filter(approved__exact=True)
    context = { "categories": categories, "tools": tools }
    return HttpResponse(template.render(context, request))
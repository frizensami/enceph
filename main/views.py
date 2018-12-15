from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from main.models import Category

# Create your views here.
def index(request):
    template = loader.get_template('main/index.html')
    categories = Category.objects.all()
    context = { "categories": categories }
    return HttpResponse(template.render(context, request))
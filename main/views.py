from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.template import loader
from main.models import Category, Tool
from django.core.exceptions import ValidationError

# Create your views here.
def index(request):
    template = loader.get_template('main/index.html')
    categories = Category.objects.all()
    tools = Tool.objects.filter(approved__exact=True)
    context = { "categories": categories, "tools": tools }
    return HttpResponse(template.render(context, request))

def add_http_to_link(link):
    if link.startswith('http') or link.startswith('https') or link.startswith('ftp') or link.startswith('ftps'):
        return link
    else:
        return "http://" + link


def new_tool(request):
    print(str(request.POST))
    tool_name = request.POST['tool_name']
    tool_link = add_http_to_link(request.POST['tool_link'])
    tool_description = request.POST['tool_description']
    tool_logo_link = add_http_to_link(request.POST['tool_logo_link'])
    is_for_developers = 'tool_is_for_developers' in request.POST
    is_beta = 'tool_is_beta' in request.POST
    tool_categories = list(request.POST.getlist('tool_categories'))
    tool = Tool(name=tool_name, link=tool_link, description=tool_description, logo=tool_logo_link, approved=False, is_for_developers=is_for_developers, is_beta=is_beta)
    try:
        tool.full_clean()
        tool.save()
        # Now we need to try to add the categories
        for category_id in tool_categories:
            tool.categories.add(category_id)
        tool.full_clean()
        tool.save()
        print(tool)
        # If successful - send email (TODO)
        return HttpResponse('Tool successfully submitted!')
    except ValidationError as e:
        print(str(e))
        return HttpResponseBadRequest('<strong> Server-side form validation error</strong>: <br> ' + str(e))
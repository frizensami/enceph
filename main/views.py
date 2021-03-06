from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.template import loader
from main.models import Category, Tool
from django.core.exceptions import ValidationError
from django.db.models import Count
import math
import json

NUM_RESULTS_PER_PAGE = 5
def return_results_for_page(xs, results_per_page, page_number):
    max_num_page = get_max_page_num(xs, results_per_page)
    if page_number < 1 or page_number > max_num_page:
        return None
    
    lowest_idx = (page_number - 1) * NUM_RESULTS_PER_PAGE
    highest_idx_exclusive = lowest_idx + NUM_RESULTS_PER_PAGE

    return xs[lowest_idx:highest_idx_exclusive]

def get_max_page_num(xs, results_per_page):
    return math.ceil(len(xs) / results_per_page)

# Create your views here.
def index(request, pagenum):
    template = loader.get_template('main/index.html')
    categories_to_filter = request.GET.getlist('categories_filter')
    target_audience = request.GET.get('targetaudience', 'all')
    dev_state = request.GET.get('devstate', 'all')
    categories = Category.objects.all()
    tools = Tool.objects.filter(approved__exact=True)
    if len(categories_to_filter) > 0:
        tools = tools.filter(categories__in=categories_to_filter).annotate(num_categs=Count('categories')).filter(num_categs=len(categories_to_filter))
    if target_audience != "all":
        if target_audience == "researchers":
            tools = tools.filter(is_for_developers__exact=False)
        elif target_audience == "developers":
            tools = tools.filter(is_for_developers__exact=True)

    if dev_state != "all":
        if dev_state == "beta":
            tools = tools.filter(is_beta__exact=True)
        elif dev_state == "released":
            tools = tools.filter(is_beta__exact=False)

    #  We do not need the submitter email - better to keep private
    tools.defer('submitter_email')

    print(tools)

    tools_to_display = return_results_for_page(tools, NUM_RESULTS_PER_PAGE, pagenum)
    
    context = { "categories": categories, "tools": tools_to_display, "cur_page_num": pagenum, "page_numbers": range(1, get_max_page_num(tools, NUM_RESULTS_PER_PAGE) + 1), "max_page_num": get_max_page_num(tools, NUM_RESULTS_PER_PAGE)}
    return HttpResponse(template.render(context, request))

def index_noarg(request):
    return index(request, 1)

def add_http_to_link(link):
    if link == None:
        return
    if link.startswith('http') or link.startswith('https') or link.startswith('ftp') or link.startswith('ftps'):
        return link
    else:
        return "http://" + link


def new_tool(request):
    print(str(request.POST))
    tool_name = request.POST.get('tool_name', None)
    tool_link = add_http_to_link(request.POST.get('tool_link', None))
    tool_description = request.POST.get('tool_description', None)
    tool_submitter_email = request.POST.get('tool_email', "")
    is_for_developers = 'tool_is_for_developers' in request.POST
    is_beta = 'tool_is_beta' in request.POST
    tool_categories = list(request.POST.getlist('tool_categories'))
    tool = Tool(name=tool_name, link=tool_link, description=tool_description, approved=False, is_for_developers=is_for_developers, submitter_email=tool_submitter_email, is_beta=is_beta)
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
        return HttpResponse('Tool successfully submitted! Please wait a while for the moderators to approve your submission.')
    except ValidationError as e:
        # print(str(e))
        return HttpResponseBadRequest(json.dumps(e.message_dict))
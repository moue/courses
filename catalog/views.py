from django.shortcuts import get_object_or_404, render_to_response
from django.template.context import RequestContext
from django.core.paginator import Paginator, InvalidPage
# from . import  SOME MODELS # '.' signifies the current directory
from collections import OrderedDict
import json
from django.conf import settings
from datetime import datetime  
import urllib
import random


# Create your views here.
def index(request):
    url = 'http://api.cs50.net/courses/3/courses?key='+settings.USER_KEYS+'&output=json'
    json_obj = json.load(urllib.urlopen(url))    

    data = json_obj
    paginator = Paginator(data, 10)
    if request.method == 'GET':
        if request.is_ajax():
            if request.GET.get('page_number'):
                # Paginate based on the page number in the GET request
                page_number = request.GET.get('page_number');
                try:
                    page_objects = paginator.page(page_number).object_list
                except InvalidPage:
                    return HttpResponseBadRequest(mimetype="json")
                # Serialize the paginated objects
                resp = serialize_debates(page_objects)
                return HttpResponse(json.dumps(resp), mimetype='json')
    courses = paginator.page(1).object_list
    print courses
    template_name = 'index.html'
    return render_to_response(template_name, locals(), context_instance = RequestContext(request))
from django.shortcuts import render, redirect
from project.models import *

#
# Functions
#

def get_item_list(max_resuls=5):
	return Item.objects.all()[:max_resuls]

#
# Views
#

def index(request):
    return render(request, 'project/index.html',
        {'item_list': get_item_list()})

def about(request):
    return render(request, 'project/about.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.http import is_safe_url
from project.models import *
from project.forms import *

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

@login_required
def category_add(request):
    form = None
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            if 'image' in request.FILES:
                form.image = request.FILES['image']
            form.save()

            return index(request)
        else:
            print form.errors
    else:
        form = CategoryForm()
    return render(request, 'project/category_add.html', {'form': form})

@login_required
def item_add(request):
    form = None
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
    else:
        form = ItemForm()

    return render(request, 'project/item_add.html', {'form': form})

@login_required
def item_list(request):
    item_list = get_item_list(max_resuls=10)
    return render(request, 'project/item_list.html', {'item_list': item_list})
    
#
# Registraton
#

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            registered = True
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()

    return render(request, 'project/register.html', {'user_form': user_form, 'registered': registered})


def user_login(request):
    redirect_to = request.REQUEST.get('next', 'index')
    if not is_safe_url(url=redirect_to, host=request.get_host()):
        redirect_to = ('index')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(redirect_to)
            else:
                return render(request, 'project/login.html', {'disabled_account': 1})
        else:
            return render(request, 'project/login.html', {'bad_details': 1})
    
    # if GET
    return render(request, 'project/login.html', {'next': redirect_to})


@login_required
def user_logout(request):
    logout(request)
    return redirect('index')

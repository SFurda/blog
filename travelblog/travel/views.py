from django.conf import settings
from django.shortcuts import render, redirect
from .models import Travel, Category, Wellness, WellnessCategory, GearCategory, Gear
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .forms import TravelForm, WellnessForm, GearForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from itertools import chain
from operator import attrgetter

# Create your views here.
def index(request):
    travel_posts = Travel.objects.all().order_by('-pub_date')
    for post in travel_posts:
        post.model_name = 'travel'
        
    wellness_posts = Wellness.objects.all().order_by('-pub_date')
    for post in wellness_posts:
        post.model_name = 'wellness'
        
    gear_posts = Gear.objects.all().order_by('-pub_date')
    for post in gear_posts:
        post.model_name = 'gear'
        
    posts = sorted(chain(travel_posts, wellness_posts, gear_posts), key=attrgetter('pub_date'), reverse=True)
    return render(request, 'travel/index.html', {'posts': posts})

def travel_post_read(request, pk):
    post = get_object_or_404(Travel, pk=pk)
    return render(request, 'travel/travel_post_read.html', {'post': post})

def wellness_post_read(request, pk):
    post = get_object_or_404(Wellness, pk=pk)
    return render(request, 'travel/wellness_post_read.html', {'post': post})

def gear_post_read(request, pk):
    post = get_object_or_404(Gear, pk=pk)
    return render(request, 'travel/gear_post_read.html', {'post': post})

def theme_view(request, template, model, category_model, category_slug=None):
    categories = category_model.objects.all()
    if category_slug:
        category = get_object_or_404(category_model, slug=category_slug)
        posts = model.objects.filter(category=category).order_by('-pub_date')
    else:
        posts = model.objects.all().order_by('-pub_date')
    return render(request, template, {'posts': posts, 'categories': categories})

@login_required
def create_post_view(request, form_class, template):
    if not request.user.is_superuser:
        return redirect(index)
    
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            form.save_m2m()
            return redirect(index)
    else:
        form = form_class()
    return render(request, template, {'form': form})

###### TRAVEL #########
def travel(request, category_slug=None):
    return theme_view(request, 'travel/travel.html', Travel, Category, category_slug)

@login_required
def create_post(request):
    return create_post_view(request, TravelForm, 'travel/createpost.html')

########## WELLNESS ############
def wellness(request, category_slug=None):
    return theme_view(request, 'travel/wellness.html', Wellness, WellnessCategory, category_slug)

@login_required
def create_wellness_post(request):
    return create_post_view(request, WellnessForm, 'travel/create_wellness_post.html')

######## GEAR ######
def gear(request, category_slug=None):
    return theme_view(request, 'travel/gear.html', Gear, GearCategory, category_slug)

@login_required
def create_gear_post(request):
    return create_post_view(request, GearForm, 'travel/create_gear_post.html')

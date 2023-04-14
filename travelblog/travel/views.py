from django.conf import settings
from django.shortcuts import render, redirect
from .models import Travel, Category, Wellness, WellnessCategory
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .forms import TravelForm, WellnessForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from itertools import chain
from operator import attrgetter

# Create your views here.
def index(request):
    travel_posts = Travel.objects.all().order_by('-pub_date')
    wellness_posts = Wellness.objects.all().order_by('-pub_date')
    posts = sorted(chain(travel_posts, wellness_posts), key=attrgetter('pub_date'), reverse=True)
    return render(request, 'travel/index.html', {'posts': posts})

###### TRAVEL #########
def travel(request, category_slug=None):
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        posts = Travel.objects.filter(category=category).order_by('-pub_date')
    else:
        posts = Travel.objects.all().order_by('-pub_date')
    return render(request, 'travel/travel.html', {'posts': posts, 'categories': categories})

@login_required
def create_post(request):
    if not request.user.is_superuser:
        return redirect(index)
    
    if request.method == 'POST':
        form = TravelForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            form.save_m2m()
            return redirect(index)  
    else:
        form = TravelForm()
    return render(request, 'travel/createpost.html', {'form': form})

########## WELLNESS ############
def wellness(request, category_slug=None):
    categories = WellnessCategory.objects.all()
    if category_slug:
        category = get_object_or_404(WellnessCategory, slug=category_slug)
        posts = Wellness.objects.filter(category=category).order_by('-pub_date')
    else:
        posts = Wellness.objects.all().order_by('-pub_date')
    return render(request, 'travel/wellness.html', {'posts': posts, 'categories': categories})

@login_required
def create_wellness_post(request):
    if not request.user.is_superuser:
        return redirect(index)
    
    if request.method == 'POST':
        form = WellnessForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            form.save_m2m()
            return redirect(index)  
    else: 
        form = WellnessForm()
    return render(request, 'travel/create_wellness_post.html', {'form': form})
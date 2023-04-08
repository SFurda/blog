from django.conf import settings
from django.shortcuts import render, redirect
from .models import Travel
from django.contrib.auth.models import User
from .forms import TravelForm
from django.utils import timezone


# Create your views here.
def index(request):
    posts = Travel.objects.all().order_by('-pub_date')
    return render(request, 'travel/index.html', {'posts': posts})

def create_post(request):
    if request.method == 'POST':
        form = TravelForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            form.save_m2m()
            return redirect(index)  # Replace with your post list URL pattern name
    else:
        form = TravelForm()
    return render(request, 'travel/createpost.html', {'form': form})
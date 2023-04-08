from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Category(models.Model):
    CATEGORY_CHOICES = [
        ('destinations', 'Destinations'),
        ('travel_tips_guides', 'Travel Tips & Guides'),
        ('adventure_travel', 'Adventure Travel'),
        ('travel_stories', 'Travel Stories'),
    ]

    name = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name

class Tag(models.Model):
    TAG_CHOICES = [
        ('solo_travel', 'Solo Travel'),
        ('budget_travel', 'Budget Travel'),
        ('group_travel', 'Group Travel'),
        ('luxury_travel', 'Luxury Travel'),
        ('road_trips', 'Road Trips'),
        ('city_breaks', 'City Breaks'),
        ('beach_getaways', 'Beach Getaways'),
        ('off_beach', 'Off Beach'),
        ('unique_spots', 'Unique Spots'),
    ]

    name = models.CharField(max_length=50, choices=TAG_CHOICES)

    def __str__(self):
        return self.name

class Travel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    youtube_url = models.URLField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    pub_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.template.defaultfilters import slugify

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class CategoryBase(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, editable=False)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def generate_slug(self):
        return slugify(self.get_name_display())

    def save(self, *args, **kwargs):
        self.slug = self.generate_slug()
        super().save(*args, **kwargs)

class TagBase(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class BaseModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    youtube_url = models.URLField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

# Travel theme
class Category(CategoryBase):
    CATEGORY_CHOICES = [
        ('Destinations', 'Destinations'),
        ('Travel Tips & Guides', 'Travel Tips & Guides'),
        ('Adventure Travel', 'Adventure Travel'),
        ('Travel Storie', 'Travel Stories'),
    ]

    name = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

class Tag(TagBase):
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

class Travel(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    pub_date = models.DateTimeField(default=timezone.now)

# Wellness theme
class WellnessCategory(CategoryBase):
    WELLNESS_CATEGORY_CHOICES = [
        ('Wellness Retreats', 'Wellness Retreats'),
        ('Mindfulness & Mental Health', 'Mindfulness & Mental Health'),
        ('Food & Nutrition', 'Food & Nutrition'),
        ('Fitness & Exercise', 'Fitness & Exercise'),
        ('Personal Wellness Storie', 'Personal Wellness Stories'),
    ]

    name = models.CharField(max_length=50, choices=WELLNESS_CATEGORY_CHOICES)

class WellnessTags(TagBase):
    WELLNESS_TAG_CHOICES = [
        ('stress_management', 'Stress Management'),
        ('mental_health', 'Mental Health'),
        ('workout', 'Workouts'),
        ('food', 'Food'),
        ('recepies', 'Recepies'),
        ('hotel_fitness', 'Hotel Fitness'),
    ]

    name = models.CharField(max_length=50, choices=WELLNESS_TAG_CHOICES)

class Wellness(BaseModel):
    category = models.ForeignKey(WellnessCategory, on_delete=models.CASCADE)
    tags = models.ManyToManyField(WellnessTags)
    pub_date = models.DateTimeField(default=timezone.now)

class GearCategory(CategoryBase):
    GEAR_CATEGORY_CHOICES = [
        ('Gear Reviews', 'Gear Reviews'),
        ('Gear Guides', 'Gear Guides'),
        ('Travel Gadgets', 'Travel Gadgets'),
        ('Outdoor Gear', 'Outdoor Gear'),
    ]

    name = models.CharField(max_length=50, choices=GEAR_CATEGORY_CHOICES)

class GearTags(TagBase):
    GEAR_TAG_CHOICES = [
        ('Backpacks', 'Backpacks'),
        ('Travel Clothing', 'Travel Clothing'),
        ('Travel Accessories', 'Travel Accessories'),
        ('Camera Gear', 'Camera Gear'),
        ('Hiking Gear', 'Hiking Gear'),
        ('Travel Tech', 'Travel Tech'),
        ('Apps', 'Apps'),
    ]

    name = models.CharField(max_length=50, choices=GEAR_TAG_CHOICES)

class Gear(BaseModel):
    category = models.ForeignKey(GearCategory, on_delete=models.CASCADE)
    tags = models.ManyToManyField(GearTags)
    pub_date = models.DateTimeField(default=timezone.now)
    image_url_1 = models.URLField(blank=True, null=True)
    image_url_2 = models.URLField(blank=True, null=True)
    image_url_3 = models.URLField(blank=True, null=True)
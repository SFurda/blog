from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.template.defaultfilters import slugify
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

######## TRAVEL THEME ##############
class Category(models.Model):
    CATEGORY_CHOICES = [
        ('destinations', 'Destinations'),
        ('travel_tips_guides', 'Travel Tips & Guides'),
        ('adventure_travel', 'Adventure Travel'),
        ('travel_stories', 'Travel Stories'),
    ]

    name = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    slug = models.SlugField(max_length=50, unique=True, editable=False)

    def __str__(self):
        return self.name

    def generate_slug(self):
        return slugify(self.get_name_display())

    def save(self, *args, **kwargs):
        self.slug = self.generate_slug()
        super().save(*args, **kwargs)

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
########## END OF TRAVEl THEME ####################

############# WELLNESS THEME ##################

class WellnessCategory(models.Model):
    WELLNESS_CATEGORY_CHOICES = [
        ('wellness_retreats', 'Wellness Retreats'),
        ('mindfulness_and_mental_health', 'Mindfulness & Mental Health'),
        ('food_and_nutrition', 'Food & Nutrition'),
        ('fitness_and_excercise', 'Fitness & Exercise'),
        ('persoanl_wellness_stories', 'Personal Wellness Stories'),
    ]

    name = models.CharField(max_length=50, choices=WELLNESS_CATEGORY_CHOICES)
    slug = models.SlugField(max_length=50, unique=True, editable=False)

    def __str__(self):
        return self.name

    def generate_slug(self):
        return slugify(self.get_name_display())

    def save(self, *args, **kwargs):
        self.slug = self.generate_slug()
        super().save(*args, **kwargs)

class WellnessTags(models.Model):
    WELLNESS_TAG_CHOICES = [
        ('stress_management', 'Stress Management'),
        ('mental_health', 'Mental Health'),
        ('workout', 'Workouts'),
        ('food', 'Food'),
        ('recepies', 'Recepies'),
        ('hteol_fitness', 'Hotel Fitness'),
        
    ]

    name = models.CharField(max_length=50, choices=WELLNESS_TAG_CHOICES)

    def __str__(self):
        return self.name

class Wellness(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    youtube_url = models.URLField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    category = models.ForeignKey(WellnessCategory, on_delete=models.CASCADE)
    tags = models.ManyToManyField(WellnessTags)
    pub_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title
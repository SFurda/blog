# Generated by Django 4.1.7 on 2023-04-14 18:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('travel', '0003_alter_category_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='WellnessCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('wellness_retreats', 'Wellness Retreats'), ('mindfulness_and_mental_health', 'Mindfulness & Mental Health'), ('food_and_nutrition', 'Food & Nutrition'), ('fitness_and_excercise', 'Fitness & Exercise'), ('persoanl_wellness_stories', 'Personal Wellness Stories')], max_length=50)),
                ('slug', models.SlugField(editable=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='WellnessTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('solo_travel', 'Stress Management'), ('budget_travel', 'Mental Health'), ('group_travel', 'Workouts'), ('luxury_travel', 'Food'), ('road_trips', 'Recepies'), ('city_breaks', 'Hotel Fitness')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Wellness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('youtube_url', models.URLField(blank=True, null=True)),
                ('image_url', models.URLField(blank=True, null=True)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.wellnesscategory')),
                ('tags', models.ManyToManyField(to='travel.tag')),
            ],
        ),
    ]

# Generated by Django 4.1.7 on 2023-04-12 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank='True', editable=False, unique=True),
        ),
    ]

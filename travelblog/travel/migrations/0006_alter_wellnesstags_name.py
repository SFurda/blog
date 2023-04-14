# Generated by Django 4.1.7 on 2023-04-14 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0005_alter_wellness_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wellnesstags',
            name='name',
            field=models.CharField(choices=[('stress_management', 'Stress Management'), ('mental_health', 'Mental Health'), ('workout', 'Workouts'), ('food', 'Food'), ('recepies', 'Recepies'), ('hteol_fitness', 'Hotel Fitness')], max_length=50),
        ),
    ]
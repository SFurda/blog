from django.urls import path
from . import views

#app_name = 'travel'

urlpatterns = [
    path('', views.index, name='index'),
    path('createpost/', views.create_post, name='createpost'),
    path('travel/',views.travel, name='travel'),
    path('travel/category/<slug:category_slug>/', views.travel, name='travel_by_category'),

    path('create_wellness_post/', views.create_wellness_post, name='create_wellness_post'),
    path('wellness/',views.wellness, name='wellness'),
    path('wellness/category/<slug:category_slug>/', views.travel, name='wellness_by_category'),
]

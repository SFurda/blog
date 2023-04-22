from django.urls import path
from . import views

#app_name = 'travel'

urlpatterns = [
    
    path('', views.index, name='index'),
    #travel urls
    path('createpost/', views.create_post, name='createpost'),
    path('travel/',views.travel, name='travel'),
    path('travel/category/<slug:category_slug>/', views.travel, name='travel_by_category'),
    #wellness urls
    path('create_wellness_post/', views.create_wellness_post, name='create_wellness_post'),
    path('wellness/',views.wellness, name='wellness'),
    path('wellness/wellness_category/<slug:category_slug>/', views.wellness, name='wellness_by_category'),
    #gear urls
    path('cteate_gear_post/', views.create_gear_post, name='create_gear_post'),
    path('gear/',views.gear, name='gear'),
    path('gear/gear_category/<slug:category_slug>/', views.gear, name='gear_by_category'),

    #read post

    path('travel/<int:pk>/', views.travel_post_read, name='travel_post_read'),
    path('wellness/<int:pk>/', views.wellness_post_read, name='wellness_post_read'),
    path('gear/<int:pk>/', views.gear_post_read, name='gear_post_read'),
   
]

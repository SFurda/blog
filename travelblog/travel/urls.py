from django.urls import path
from . import views

#app_name = 'travel'

urlpatterns = [
    path('', views.index, name='index'),
    path('createpost/', views.create_post, name='createpost'),
    path('travel/',views.travel, name='travel'),
    path('travel/category/<slug:category_slug>/', views.travel, name='travel_by_category'),
]

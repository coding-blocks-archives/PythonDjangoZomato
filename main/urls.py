from django.urls import path
from django.contrib.auth.decorators import login_required

from main import views

urlpatterns = [
  path('', views.Index.as_view()),
  path(
    'restaurant/<int:pk>', 
    views.Restaurant.as_view(), 
    name = 'restaurant'),
  path('restaurant/<int:pk>/add_review', views.add_review, name = 'restaurant_review')

]

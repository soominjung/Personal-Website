from django.urls import path
from mainpage import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
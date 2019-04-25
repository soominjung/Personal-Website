from django.urls import path
from mainpage import views

urlpatterns = [
    path('mainpage/', views.post_list, name='post_list'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('gym/', views.GymList.as_view(), name="gym_list"),
    path('gym/new/', views.GymCreate.as_view(), name="gym_create"),
    path('gym/<int:pk>/', views.GymDetail.as_view(), name="gym_detail"),
    path('gym/<int:pk>/update',
         views.GymUpdate.as_view(), name="gym_update"),

]
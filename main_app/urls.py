from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    # path('gyms/', views.GymsList.as_view(), name="gyms_list"),
]
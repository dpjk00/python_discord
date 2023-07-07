from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('channel/<str:pk>/', views.channel, name="channel")
]
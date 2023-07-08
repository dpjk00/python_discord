from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('channel/<str:pk>/', views.channel, name="channel"),

    path('create-channel/', views.create_channel, name="create_channel"),
    path('update-channel/<str:pk>/', views.update_channel, name="update_channel"),
    path('delete-channel/<str:pk>/', views.delete_channel, name="delete_channel"),
]
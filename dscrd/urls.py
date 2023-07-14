from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),

    path('', views.home, name="home"),
    path('channel/<str:pk>/', views.channel, name="channel"),

    path('create-channel/', views.create_channel, name="create_channel"),
    path('update-channel/<str:pk>/', views.update_channel, name="update_channel"),
    path('delete-channel/<str:pk>/', views.delete_channel, name="delete_channel"),
    path('delete-message/<str:pk>/', views.delete_message, name="delete_message"),
]
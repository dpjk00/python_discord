from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_routes),
    path('channels/', views.get_channels),
    path('channels/<str:pk>', views.get_channel),
    path('registration', views.registration_view),
    path('users/', views.get_users),
    path('login', views.login_view),
]
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('rooms/', views.rooms, name='rooms'),
    path('rooms/<slug:slug>/', views.room, name='room'),
]
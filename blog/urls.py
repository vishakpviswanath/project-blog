from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views



urlpatterns = [

    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login_page.html'), name='login'),
    path('new_home/', views.home, name='home'), 
]
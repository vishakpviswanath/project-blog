from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views



urlpatterns = [

    path('',views.first_page, name='first_page'),
    path('post/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login_page.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('register/', views.register, name='register' ),
    path('profile/', views.profile, name='profile'),
    path('author_profile/<str:username>/', views.author_profile, name='author_profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('change-password/', views.change_password, name='change_password'),
]
"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from likelion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.intro ,name='intro'),
    path('login_action/', views.login_action ,name='login_action'),
    path('check_action/',views.check_action,name='check_action'),
    path('register/', views.register, name='register'),
    path('register_action/', views.register_action, name='register_action'),
    path('view/', views.view, name='view'),
    path('check/', views.check, name='check'),
    path('register_check/', views.register_check, name='register_check'),
]

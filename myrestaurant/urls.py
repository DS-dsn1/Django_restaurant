"""myrestaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from restaurant import views
from .router import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dish/', include('restaurant.urls')),
    path('', views.index, name='index'),
    path('chef', views.show_chef, name='chefs'),
    path('customer/', views.customer_list, name='customer_list'),
    path('api/', include(router.urls), name='api'),
]

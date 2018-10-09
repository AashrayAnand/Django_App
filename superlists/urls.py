"""superlists URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path, include
from lists import views as list_views
from lists import urls as list_urls

urlpatterns = [
    # maps regex rout to the home_page view
    re_path(r'^$', list_views.home_page, name='home'),
    # we can include all list urls from the separate urls
    # file in lists, and use the below path as a prefix for
    # those urls, with the remaining suffix being in the list
    # urls file
    re_path(r'^lists/', include(list_urls)),
]

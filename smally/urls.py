"""smally URL Configuration

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
from django.urls import path
from oneapp.views import (validate_url, shorten_view,
                          success_view, url_redirection_view)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', shorten_view, name='shorten'),
    path('success/<slug:data>', success_view, name='success_page'),
    path('ajax/validate_url/', validate_url, name='validate_url'),
    path('<slug:new_short_url>', url_redirection_view, name='redirection'),
]

"""
URL configuration for octettechnology project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from octet import views  # Import views from your app


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index.html', views.index),
    path('service.html', views.service),
    path('about.html', views.about),
    path('contact.html', views.contact),
    path('contact.html', views.contact),
    path('quote.html', views.quote),
    path('price.html', views.price),
    path('team.html', views.team),
    path('testimonial.html', views.testimonial),
    path('feature.html', views.feature),
    path('detail.html', views.detail),
    path('blog.html', views.blog),
    
    
    
    
    
    
    

    # other paths...
]
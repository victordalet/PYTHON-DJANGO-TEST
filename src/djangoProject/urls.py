from django.contrib import admin
from django.urls import path

from djangoProject.views import index, formPage, home

urlpatterns = [
    path('', index),
    path('form', formPage),
    path('home', home),
    path('admin/', admin.site.urls)
]

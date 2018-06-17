from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='app1_index'),
    path('form/', views.display_form, name='display_form'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.simple_upload, name='simple_upload'),
    path('model_upload/', views.model_form_upload, name='model_form_upload')
]

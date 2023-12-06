from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_form, name = "upload_form"),
    path('new_project', views.project_form, name = "project_form"),
]
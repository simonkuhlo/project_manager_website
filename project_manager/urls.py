from django.urls import path
from . import views

urlpatterns = [
    path('', views.formviews.upload_form, name = "upload_form"),
    path('new_project', views.formviews.project_form, name = "project_form"),
]
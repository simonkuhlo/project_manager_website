from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('home', views.views.homescreen, name = "home"),
    path('new_project', views.formviews.project_form, name = "project_form"),
    path('project_list', views.views.project_list, name = "project_list"),
    path('project:<str:pk>/', views.views.project_details, name = "project_list"),
]
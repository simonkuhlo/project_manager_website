from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_projects, name = "list_projects"),
    path('id:<str:pk>/', views.single_key, name = "single_key"),
]
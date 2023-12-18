from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.formviews.upload_form, name = "upload_form"),
    path('new_project', views.formviews.project_form, name = "project_form"),
    path('project_list', views.views.project_list, name = "project_list"),
    path('project:<str:pk>/', views.views.project_details, name = "project_list"),
]
# Serving the media files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()
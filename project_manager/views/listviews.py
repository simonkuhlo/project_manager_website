from django.shortcuts import render
from django.http import HttpResponseRedirect
from .. import models

def project_list(request):
    projects = models.Project.objects.all()
    ctx = {"project_list" : projects}
    return render(request, 'project_manager/project_list.html', ctx)
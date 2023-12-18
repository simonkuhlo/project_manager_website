from django.shortcuts import render
from django.http import HttpResponseRedirect
from .. import models


def homescreen(request):
    return render(request, 'project_manager/home.html')

def project_list(request):
    projects = models.Project.objects.all()
    ctx = {"project_list" : projects}
    return render(request, 'project_manager/project_list.html', ctx)

def project_details(request, id):
    project = models.Project.objects.get(id=id)
    ctx = {"project" : project}
    return render(request, 'project_manager/project_details.html', ctx)
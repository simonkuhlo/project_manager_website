from django.shortcuts import render
from django.http import HttpResponseRedirect
from .. import models

def all_keys(request):
    projects = models.Project.objects.all()
    ctx = {"project_list" : projects}
    return render(request, 'project_manager/all_keys.html', ctx)

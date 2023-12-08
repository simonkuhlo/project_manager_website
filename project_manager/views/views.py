from django.shortcuts import render
from django.http import HttpResponseRedirect
from .. import models


def project_details(request, id):
    project = models.Project.objects.get(id=id)
    ctx = {"project" : project}
    return render(request, 'project_manager/project_details.html', ctx)
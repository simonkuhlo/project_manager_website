from django.shortcuts import render
from django.http import HttpResponseRedirect
from .. import forms

def upload_form(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        submission = forms.UploadForm(request.POST, request.FILES)
        # check whether it's valid:
        if submission.is_valid():
            # process the data in form.cleaned_data as required
            # Create a form instance from POST data.
            new_upload = submission.save()
            # redirect to a new URL:
        else:
            print(submission.errors)
            return HttpResponseRedirect("/error/")
    # if a GET (or any other method) we'll create a blank form
    #else:
    form = forms.UploadForm()

    return render(request, "project_manager/forms/upload_form.html", {"form": form})


def project_form(request):
    if request.method == "POST":
        submission = forms.ProjectForm(request.POST, request.FILES)
        if submission.is_valid():
            new_upload = submission.save()
        else:
            print(submission.errors)
            return HttpResponseRedirect("/error/")
    form = forms.ProjectForm()
    return render(request, "project_manager/forms/new_project.html", {"form": form})
from django.forms import ModelForm
from . import models

class UploadForm(ModelForm):
    class Meta:
        model = models.FileUpload
        exclude = []
        
class ProjectForm(ModelForm):
    class Meta:
        model = models.Project
        exclude = []
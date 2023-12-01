from django.forms import ModelForm
from . import models

class UploadForm(ModelForm):
    class Meta:
        model = models.FileUpload
        exclude = []
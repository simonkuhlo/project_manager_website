from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
# Create your models here.


class FileUpload(models.Model):
    name = models.CharField(max_length=100)
    # file will be uploaded to MEDIA_ROOT/uploads
    imge = models.ImageField(upload_to = "upload/")

    #class Meta:
        #ordering = ['-updated', 'created']

    def __str__(self):
        return(str(self.name))
    
    
class Project(models.Model):
    class status_choices(models.TextChoices):
        not_started = "not_started", _("Not started")
        planning = "planning", _("Planning")
        ongoing = "ongoing", _("Ongoing")
        paused = "paused", _("Paused")
        finished = "finished", _("Finished")
        dropped = "dropped", _("Dropped")
         
    name = models.CharField(max_length=100)
    description = models.TextField()
    thumbnail_image = models.ImageField(upload_to="upload/")
    status = models.CharField(max_length = 11, choices = status_choices.choices, default = status_choices.not_started)
    current_version = models.IntegerField(default=1)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
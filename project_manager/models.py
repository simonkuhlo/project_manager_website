from django.db import models
from django.conf import settings

# Create your models here.


class FileUpload(models.Model):
    name = models.CharField(max_length=100)
    # file will be uploaded to MEDIA_ROOT/uploads
    imge = models.ImageField(upload_to = "upload/")

    #class Meta:
        #ordering = ['-updated', 'created']

    def __str__(self):
        return(str(self.name))
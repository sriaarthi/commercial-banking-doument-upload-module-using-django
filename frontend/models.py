from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100)
    # file will be uploaded to MEDIA_ROOT/uploads
    upload = models.FileField(upload_to='uploads/')

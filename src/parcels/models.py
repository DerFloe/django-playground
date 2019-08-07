from django.db import models

# Create your models here.

class Parcel(models.Model):
    title = models.CharField(max_length=120)
    notes = models.TextField()
    trackingNr = models.CharField(max_length=120)

    def __str__(self):
        return self.title
from django.db import models


# Create your models here.
class Locations(models.Model):
    location_id = models.CharField(max_length=20)
    location_name = models.CharField(max_length=200)
  
    def __str__(self):
        return f"{self.location_name}"
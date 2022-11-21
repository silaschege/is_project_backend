from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class ManufactureRegisterModel(models.Model):
    manufactureName = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    country = models.CharField(max_length=255)
    county = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    user = models.ManyToManyField(User)
    
    def __str__(self):
        return self.manufactureName
    

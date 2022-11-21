from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# # Create your models here.


class LandRegisterModel(models.Model):
  country = models.CharField(max_length=255) 
  sub_county = models.CharField(max_length=255)
  village = models.CharField(max_length=255)
  landSize = models.IntegerField()
  user_id = models.ManyToManyField(User)

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BrandProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  tel = models.CharField(max_length=255)
  company = models.CharField(max_length=255)
  position = models.CharField(max_length=255)


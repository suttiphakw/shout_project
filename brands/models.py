from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BrandProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  email = models.EmailField(max_length=255, default=None)
  first_name = models.CharField(max_length=255, default=None)
  last_name = models.CharField(max_length=255, default=None)
  tel = models.CharField(max_length=255, default=None)
  company = models.CharField(max_length=255, default=None)
  position = models.CharField(max_length=255, default=None)

  def __str__(self):
    return self.company


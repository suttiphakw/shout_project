from pyexpat import model
from statistics import mode
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Campaign(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)

  # Campaign Info
  campaign_name = models.CharField(max_length=255)

  # Datetime
  campaign_created = models.DateTimeField(default=now, editable=False)
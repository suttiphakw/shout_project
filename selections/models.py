from django.db import models
from campaigns.models import Campaign
from shouters.models import Shouter


# Create your models here.
class Selection(models.Model):
  campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
  shouter = models.ForeignKey(Shouter, on_delete=models.CASCADE)

  def __str__(self):
    return self.shouter

from django.db import models
from campaigns.models import Campaign
from shouters.models import Shouter


# Create your models here.
class Selection(models.Model):
  campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
  shouter = models.ForeignKey(Shouter, on_delete=models.CASCADE)
  score = models.FloatField(null=True, blank=True)

  def __str__(self):
    if self.shouter:
      return f"{self.shouter}"
    else:
      return "Shouter Profile"

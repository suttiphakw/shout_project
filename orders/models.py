from django.db import models
from campaigns.models import Campaign
from shouters.models import Shouter


# Create your models here.
class Order(models.Model):

  # Status
  campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
  shouter = models.ForeignKey(Shouter, on_delete=models.CASCADE)
  is_selected = models.BooleanField(default=False)

  # Info
  brand_price = models.IntegerField(null=True, blank=True)
  shouter_price = models.IntegerField(null=True, blank=True)
  cpr = models.FloatField(null=True, blank=True)
  score = models.FloatField(null=True, blank=True)

  # Instagram Basic
  ig_follower_count = models.IntegerField(null=True, blank=True)
  ig_following_count = models.IntegerField(null=True, blank=True)
  ig_media_count = models.IntegerField(null=True, blank=True)

  # Instagram Insight
  ig_average_total_like = models.IntegerField(null=True, blank=True, verbose_name="IG => AVERAGE LIKE")
  ig_engagement_percent = models.FloatField(null=True, blank=True, verbose_name="IG => LIKE PERCENTAGE")
  ig_active_follower = models.IntegerField(null=True, blank=True)
  ig_active_follower_percent = models.FloatField(null=True, blank=True)
  ig_story_view = models.IntegerField(null=True, blank=True, verbose_name="IG => AVERAGE STORY VIEW")
  ig_ad_post_reach = models.IntegerField(null=True, blank=True, verbose_name="FINAL => EST AD POST REACH")
  ig_audience_male_percent = models.FloatField(null=True, blank=True, verbose_name="AUDIENCE MALE")
  ig_audience_female_percent = models.FloatField(null=True, blank=True, verbose_name="AUDIENCE FEMALE")
  ig_audience_undefined_percent = models.FloatField(null=True, blank=True, verbose_name="AUDIENCE UNDEFINED")
  ig_age_range_13_17 = models.FloatField(null=True, blank=True, verbose_name="AUDIENCE 13-17")
  ig_age_range_18_24 = models.FloatField(null=True, blank=True, verbose_name="AUDIENCE 18-24")
  ig_age_range_25_34 = models.FloatField(null=True, blank=True, verbose_name="AUDIENCE 25-34")
  ig_age_range_35_44 = models.FloatField(null=True, blank=True, verbose_name="AUDIENCE 35-44")
  ig_age_range_45_54 = models.FloatField(null=True, blank=True, verbose_name="AUDIENCE 45-54")
  ig_age_range_55_64 = models.FloatField(null=True, blank=True, verbose_name="AUDIENCE 55-64")
  ig_audience_location_1 = models.CharField(max_length=120, null=True, blank=True, verbose_name="AUDIENCE LOCATION #1")
  ig_audience_location_1_percent = models.FloatField(null=True, blank=True, verbose_name="AUDIENCE LOCATION #1 PERCENT")
  ig_audience_location_2 = models.CharField(max_length=120, null=True, blank=True, verbose_name="AUDIENCE LOCATION #2")
  ig_audience_location_2_percent = models.FloatField(null=True, blank=True, verbose_name="AUDIENCE LOCATION #2 PERCENT")

  def __str__(self):
    return f"{self.campaign} - {self.shouter.ig_username}'s order"

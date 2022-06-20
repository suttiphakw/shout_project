from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

from .utils.calculate import cal, cal_fb


class Campaign(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  # # Campaign Info
  # Campaign Name
  campaign_name = models.CharField(max_length=255)
  # Campaign Scope & Budget
  campaign_is_ig = models.BooleanField(default=False)
  campaign_is_fb = models.BooleanField(default=False)
  campaign_is_tiktok = models.BooleanField(default=False)
  campaign_is_twitter = models.BooleanField(default=False)
  campaign_budget = models.IntegerField(null=True, blank=True)
  campaign_work_type = models.CharField(max_length=255, null=True, blank=True)
  campaign_content_type_story = models.CharField(max_length=255, null=True, blank=True)
  campaign_fc_story_count = models.IntegerField(null=True, blank=True)
  campaign_content_type_post = models.CharField(max_length=255, null=True, blank=True)

  # Campaign Estimate
  estimate_min_reach = models.IntegerField(null=True, blank=True)
  estimate_max_reach = models.IntegerField(null=True, blank=True)
  estimate_min_shouter = models.IntegerField(null=True, blank=True)
  estimate_max_shouter = models.IntegerField(null=True, blank=True)
  estimate_min_cpr = models.FloatField(null=True, blank=True)
  estimate_max_cpr = models.FloatField(null=True, blank=True)
  # Estimate Time
  estimate_time = models.IntegerField(null=True, blank=True)

  # Datetime
  campaign_created = models.DateTimeField(default=now, editable=False)

  def __str__(self):
    return self.campaign_name

  def save(self, *args, **kwargs):
    if self.campaign_budget:
      if self.campaign_is_ig and not self.campaign_is_fb:
        response = cal(self.campaign_budget)
      else:
        response = cal_fb(self.campaign_budget)
      if self.campaign_work_type == "story":
        self.estimate_min_reach = response['min_story_reach']
        self.estimate_max_reach = response['max_story_reach']
        self.estimate_min_shouter = response['min_story_shouter']
        self.estimate_max_shouter = response['max_story_shouter']
        self.estimate_min_cpr = response['min_story_cpr']
        self.estimate_max_cpr = response['max_story_cpr']
      elif self.campaign_work_type == "post":
        self.estimate_min_reach = response['min_post_reach']
        self.estimate_max_reach = response['max_post_reach']
        self.estimate_min_shouter = response['min_post_shouter']
        self.estimate_max_shouter = response['max_post_shouter']
        self.estimate_min_cpr = response['min_post_cpr']
        self.estimate_max_cpr = response['max_post_cpr']
      else:
        self.estimate_min_reach = response['min_story_post_reach']
        self.estimate_max_reach = response['max_story_post_reach']
        self.estimate_min_shouter = response['min_story_post_shouter']
        self.estimate_max_shouter = response['max_story_post_shouter']
        self.estimate_min_cpr = response['min_story_post_cpr']
        self.estimate_max_cpr = response['max_story_post_cpr']

      self.estimate_time = 1

    super(Campaign, self).save(*args, **kwargs)

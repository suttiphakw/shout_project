from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

from .utils.calculate import (min_story_shouter,
                              max_story_shouter,
                              min_post_shouter,
                              max_post_shouter,
                              min_story_post_shouter,
                              max_story_post_shouter,
                              min_story_reach,
                              max_story_reach,
                              min_post_reach,
                              max_post_reach,
                              min_story_post_reach,
                              max_story_post_reach)

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
  campaign_content_type_post = models.CharField(max_length=255, null=True, blank=True)

  # # Campaign Result
  cal_number_shouter_min = models.IntegerField(null=True, blank=True)
  cal_number_shouter_max = models.IntegerField(null=True, blank=True)
  cal_estimate_reach_min = models.IntegerField(null=True, blank=True)
  cal_estimate_reach_max = models.IntegerField(null=True, blank=True)
  cal_cpr_min = models.FloatField(null=True, blank=True)
  cal_cpr_max = models.FloatField(null=True, blank=True)

  # Datetime
  campaign_created = models.DateTimeField(default=now, editable=False)

  def __str__(self):
    return self.campaign_name


  def save(self, *args, **kwargs):
    # IG Only
    if self.campaign_budget and self.campaign_is_ig and not self.campaign_is_fb and self.campaign_work_type == "story":
      # Shouter
      self.cal_number_shouter_min = min_story_shouter(self.campaign_budget)
      self.cal_number_shouter_max = max_story_shouter(self.campaign_budget)
      # Reach
      self.cal_estimate_reach_min =min_story_reach(self.campaign_budget)
      self.cal_estimate_reach_max = max_story_reach(self.campaign_budget)
      # CPR
      self.cal_cpr_min = round((self.campaign_budget/max_story_reach(self.campaign_budget)),2)
      self.cal_cpr_max = round((self.campaign_budget/min_story_reach(self.campaign_budget)),2)
    if self.campaign_budget and self.campaign_is_ig and not self.campaign_is_fb and self.campaign_work_type == "post":
      # Shouter
      self.cal_number_shouter_min = min_post_shouter(self.campaign_budget)
      self.cal_number_shouter_max = max_post_shouter(self.campaign_budget)
      # Reach
      self.cal_estimate_reach_min = min_post_reach(self.campaign_budget)
      self.cal_estimate_reach_max = max_post_reach(self.campaign_budget)
      # CPR
      self.cal_cpr_min = round((self.campaign_budget / max_post_reach(self.campaign_budget)), 2)
      self.cal_cpr_max = round((self.campaign_budget / min_post_reach(self.campaign_budget)), 2)
    if self.campaign_budget and self.campaign_is_ig and not self.campaign_is_fb and self.campaign_work_type == "story_post":
      # Shouter
      self.cal_number_shouter_min = min_story_post_shouter(self.campaign_budget)
      self.cal_number_shouter_max = max_story_post_shouter(self.campaign_budget)
      # Reach
      self.cal_estimate_reach_min = min_story_post_reach(self.campaign_budget)
      self.cal_estimate_reach_max = max_story_post_reach(self.campaign_budget)
      # CPR
      self.cal_cpr_min = round((self.campaign_budget / max_story_post_reach(self.campaign_budget)), 2)
      self.cal_cpr_max = round((self.campaign_budget / min_story_post_reach(self.campaign_budget)), 2)

    # IG + FB
    if self.campaign_budget and self.campaign_is_ig and self.campaign_is_fb and self.campaign_work_type == "story":
      # Shouter
      self.cal_number_shouter_min = min_story_shouter(self.campaign_budget)/1.1
      self.cal_number_shouter_max = max_story_shouter(self.campaign_budget)/1.1
      # Reach
      self.cal_estimate_reach_min =min_story_reach(self.campaign_budget)/1.1
      self.cal_estimate_reach_max = max_story_reach(self.campaign_budget)/1.1
      # CPR
      self.cal_cpr_min = round((self.campaign_budget/max_story_reach(self.campaign_budget))/1.1, 2)
      self.cal_cpr_max = round((self.campaign_budget/min_story_reach(self.campaign_budget))/1.1, 2)
    if self.campaign_budget and self.campaign_is_ig and self.campaign_is_fb and self.campaign_work_type == "post":
      # Shouter
      self.cal_number_shouter_min = min_post_shouter(self.campaign_budget)/1.1
      self.cal_number_shouter_max = max_post_shouter(self.campaign_budget)/1.1
      # Reach
      self.cal_estimate_reach_min = min_post_reach(self.campaign_budget)/1.1
      self.cal_estimate_reach_max = max_post_reach(self.campaign_budget)/1.1
      # CPR
      self.cal_cpr_min = round((self.campaign_budget / max_post_reach(self.campaign_budget))/1.1, 2)
      self.cal_cpr_max = round((self.campaign_budget / min_post_reach(self.campaign_budget))/1.1, 2)
    if self.campaign_budget and self.campaign_is_ig and self.campaign_is_fb and self.campaign_work_type == "story_post":
      # Shouter
      self.cal_number_shouter_min = min_story_post_shouter(self.campaign_budget)
      self.cal_number_shouter_max = max_story_post_shouter(self.campaign_budget)
      # Reach
      self.cal_estimate_reach_min = min_story_post_reach(self.campaign_budget)
      self.cal_estimate_reach_max = max_story_post_reach(self.campaign_budget)
      # CPR
      self.cal_cpr_min = round((self.campaign_budget / max_story_post_reach(self.campaign_budget))/1.1, 2)
      self.cal_cpr_max = round((self.campaign_budget / min_story_post_reach(self.campaign_budget))/1.1, 2)
    # Override Save
    super(Campaign, self).save(*args, **kwargs)
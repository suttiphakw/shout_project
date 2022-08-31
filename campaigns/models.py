from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.contrib.postgres.fields import ArrayField

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
  # campaign_fc_story_count = models.IntegerField(null=True, blank=True)
  campaign_content_type_post = models.CharField(max_length=255, null=True, blank=True)

  # Campaign Estimate
  estimate_min_reach = models.IntegerField(null=True, blank=True)
  estimate_max_reach = models.IntegerField(null=True, blank=True)
  estimate_min_shouter = models.IntegerField(null=True, blank=True)
  estimate_max_shouter = models.IntegerField(null=True, blank=True)
  estimate_min_cpr = models.FloatField(null=True, blank=True)
  estimate_max_cpr = models.FloatField(null=True, blank=True)

  # Campaign Product
  product_name = models.CharField(max_length=255, null=True, blank=True)
  product_photo_1 = models.ImageField(upload_to='campaign/product/', blank=True)
  product_photo_2 = models.ImageField(upload_to='campaign/product/', blank=True)
  product_photo_3 = models.ImageField(upload_to='campaign/product/', blank=True)
  product_detail = models.CharField(max_length=500, null=True, blank=True)
  product_link = models.URLField(null=True, blank=True)

  # Target
  campaign_gender = models.CharField(max_length=255, null=True, blank=True)
  campaign_age = ArrayField(models.CharField(max_length=200, null=True, blank=True), null=True, blank=True)
  campaign_province = models.CharField(max_length=255, null=True, blank=True)
  campaign_interest = ArrayField(models.CharField(max_length=200, null=True, blank=True), null=True, blank=True)
  shouter_gender = ArrayField(models.CharField(max_length=200, null=True, blank=True), null=True, blank=True)

  # Operation
  service_type = models.CharField(max_length=255, null=True, blank=True)
  service_name = models.CharField(max_length=255, null=True, blank=True)
  operation_photo = models.ImageField(upload_to='campaign/operation/', null=True, blank=True)
  service_detail = models.JSONField(null=True, blank=True)
  shouter_post_date = models.DateField(null=True, blank=True)

  # Brief
  brief_detail = models.CharField(max_length=1000, null=True, blank=True)
  brief_photo = models.ImageField(upload_to='campaign/brief/photo/', null=True, blank=True)
  brief_caption = models.CharField(max_length=1000, null=True, blank=True)
  brief_ref_photo = models.ImageField(upload_to='campaign/brief/photo/', null=True, blank=True)

  # Estimate Time
  # estimate_time = models.IntegerField(null=True, blank=True)

  # Datetime
  campaign_created = models.DateTimeField(default=now, editable=False)

  # status (draft, in_progress, finished)
  campaign_status = models.CharField(max_length=255, null=True, blank=True, default='draft')
  campaign_phase = models.IntegerField(null=True, blank=True)

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

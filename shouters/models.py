from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Shouter(models.Model):

    # Personal Info
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # # Facebook
    fb_access_token = models.CharField(max_length=500, null=True, blank=True)
    fb_access_token_created = models.DateTimeField(default=now)
    fb_page_id = models.CharField(max_length=120, null=True, blank=True)
    #
    # # Instagram
    ig_business_account_id = models.CharField(max_length=120, null=True, blank=True)
    ig_username = models.CharField(max_length=120, null=True, blank=True)
    ig_follower_count = models.IntegerField(null=True, blank=True)
    ig_active_follower = models.IntegerField(null=True, blank=True)
    ig_active_follower_harmonic = models.IntegerField(null=True, blank=True)
    ig_estimated_reach = models.IntegerField(null=True, blank=True)
    # ig_profile_picture
    # ig_post_permalink
    ig_total_like = models.IntegerField(null=True, blank=True)
    ig_average_total_like = models.IntegerField(null=True, blank=True)
    ig_like_engagement = models.IntegerField(null=True, blank=True)
    #
    # # Insight
    ig_insight = models.JSONField(null=True, blank=True)
    ig_max_total_people = models.IntegerField(null=True, blank=True)
    ig_two_most_common_city = models.JSONField(null=True, blank=True)
    ig_two_most_common_country = models.JSONField(null=True, blank=True)
    ig_two_most_common_gender_age = models.JSONField(null=True, blank=True)
    ig_audience_male_percent = models.FloatField(null=True, blank=True)
    ig_audience_female_percent = models.FloatField(null=True, blank=True)
    ig_age_range_13_17 = models.FloatField(null=True, blank=True)
    ig_age_range_18_24 = models.FloatField(null=True, blank=True)
    ig_age_range_25_34 = models.FloatField(null=True, blank=True)
    ig_age_range_35_44 = models.FloatField(null=True, blank=True)
    ig_age_range_45_54 = models.FloatField(null=True, blank=True)
    ig_age_range_55_64 = models.FloatField(null=True, blank=True)

    #
    # # Dashboard
    #
    #
    # # Performance
    #
    #
    # # History Work

    def __str__(self):
        return self.user.username

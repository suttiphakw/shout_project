from django.db import models
# from django.contrib.postgres.fields import ArrayField
from django.utils.timezone import now

# Create your models here.
class Shouter(models.Model):

    # Personal Info
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    gender = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)
    age = models.IntegerField(null=True, blank=True)
    phone = models.CharField(max_length=120)
    # interest = ArrayField(models.CharField(max_length=120), default=list)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_register = models.BooleanField(default=False)
    is_connect_ig = models.BooleanField(default=False)
    is_approve = models.BooleanField(default=False)

    # Line
    line_access_token = models.CharField(max_length=500)
    line_access_token_updated = models.DateTimeField(default=now)
    line_id_token = models.CharField(max_length=500)
    line_id_token_updated = models.DateTimeField(default=now)
    line_user_id = models.CharField(max_length=120)
    line_username = models.CharField(max_length=120)
    line_profile_picture = models.CharField(max_length=200)

    # # Facebook
    fb_access_token = models.CharField(max_length=500)
    fb_access_token_created = models.DateTimeField(default=now)
    fb_page_id = models.CharField(max_length=120)
    #
    # # Instagram
    ig_business_account_id = models.CharField(max_length=120)
    ig_username = models.CharField(max_length=120)
    ig_follower_count = models.IntegerField()
    ig_active_follower = models.IntegerField()
    ig_active_follower_harmonic = models.IntegerField()
    ig_estimated_reach = models.IntegerField()
    # ig_profile_picture
    # ig_post_permalink
    ig_total_like = models.IntegerField()
    ig_average_total_like = models.IntegerField()
    ig_like_engagement = models.IntegerField()
    #
    # # Insight
    ig_insight = models.JSONField()
    ig_max_total_people = models.IntegerField()
    ig_two_most_common_city = models.JSONField()
    ig_two_most_common_country = models.JSONField()
    ig_two_most_common_gender_age = models.JSONField()
    ig_audience_male_percent = models.FloatField()
    ig_audience_female_percent = models.FloatField()
    ig_age_range_13_17 = models.FloatField()
    ig_age_range_18_24 = models.FloatField()
    ig_age_range_25_34 = models.FloatField()
    ig_age_range_35_44 = models.FloatField()
    ig_age_range_45_54 = models.FloatField()
    ig_age_range_55_64 = models.FloatField()

    #
    # # Dashboard
    #
    #
    # # Performance
    #
    #
    # # History Work

    def __str__(self):
        return self.first_name

from django.db import models
from django.utils.timezone import now

# Create your models here.
class Shouter(models.Model):

    # Personal Info
    first_name = models.CharField(max_length=120, null=True, blank=True)
    is_register = models.BooleanField(default=False)
    is_connect_ig = models.BooleanField(default=False)

    # # Line Token
    line_access_token = models.CharField(max_length=500, null=True, blank=True)
    line_access_token_updated = models.DateTimeField(default=now)
    line_id_token = models.CharField(max_length=500, null=True, blank=True)
    line_id_token_updated = models.DateTimeField(default=now)

    # # Line User Information
    line_user_id = models.CharField(max_length=100, null=True, blank=True)
    line_username = models.CharField(max_length=100, null=True, blank=True)
    line_profile_picture = models.URLField(max_length=500, null=True, blank=True)

    # # Facebook
    fb_access_token = models.CharField(max_length=500, null=True, blank=True)
    fb_access_token_created = models.DateTimeField(default=now)
    fb_page_id = models.CharField(max_length=120, null=True, blank=True)
    fb_is_connect = models.BooleanField(default=False)

    # # Instagram
    ig_business_account_id = models.CharField(max_length=120, null=True, blank=True)
    ig_username = models.CharField(max_length=120, null=True, blank=True)
    ig_media_count = models.IntegerField(null=True, blank=True)
    ig_follower_count = models.IntegerField(null=True, blank=True)
    ig_following_count = models.IntegerField(null=True, blank=True)
    ig_active_follower = models.IntegerField(null=True, blank=True)
    ig_active_follower_harmonic = models.IntegerField(null=True, blank=True)
    ig_active_follower_percent = models.FloatField(null=True, blank=True)
    ig_estimated_reach = models.IntegerField(null=True, blank=True)
    ig_profile_picture = models.URLField(max_length=500, null=True, blank=True)

    # ig_post_permalink
    ig_total_like = models.IntegerField(null=True, blank=True)
    ig_average_total_like = models.IntegerField(null=True, blank=True)
    ig_engagement_percent = models.FloatField(null=True, blank=True)
    ig_story_view = models.FloatField(null=True, blank=True)
    ig_average_post_reach = models.FloatField(null=True, blank=True)
    # ig_like_engagement = models.IntegerField(null=True, blank=True)

    # # Pricing
    ig_price_story_fc = models.FloatField(null=True, blank=True)
    ig_price_story_ugc = models.FloatField(null=True, blank=True)
    ig_price_post_fc = models.FloatField(null=True, blank=True)
    ig_price_post_ugc = models.FloatField(null=True, blank=True)

    ig_price_story_post_fc = models.FloatField(null=True, blank=True)
    ig_price_story_post_ugc = models.FloatField(null=True, blank=True)

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
        return self.first_name

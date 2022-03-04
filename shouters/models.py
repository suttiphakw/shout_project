from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.timezone import now
from django.db.models.signals import pre_save, post_save
from shouters.lineMessagingApi.adminApproveApi import (api__admin_approve_text_message,
                                                       api__admin_approve_flex_message,
                                                       api__admin_approve_image_message)
from shouters.refresh_data import refresh_shouters
from shouters.utils.refresh.refresh_instagram import ig_photo

import requests

# Create your models here.
class Shouter(models.Model):

    # Personal Info
    nickname = models.CharField(max_length=120, null=True, blank=True)
    first_name = models.CharField(max_length=120, null=True, blank=True)
    last_name = models.CharField(max_length=120, null=True, blank=True)
    email = models.EmailField(max_length=120, null=True, blank=True)
    tel = models.CharField(max_length=120, null=True, blank=True)
    gender = models.CharField(max_length=120, null=True, blank=True)
    birthday_date = models.CharField(max_length=120, null=True, blank=True)
    birthday_month = models.CharField(max_length=120, null=True, blank=True)
    birthday_year = models.CharField(max_length=120, null=True, blank=True)
    province = models.CharField(max_length=120, null=True, blank=True)
    education = models.CharField(max_length=120, null=True, blank=True)
    college = models.CharField(max_length=120, null=True, blank=True)
    interest = ArrayField(models.CharField(max_length=200, null=True, blank=True), null=True, blank=True)

    # # Bank Account
    id_card_photo = models.ImageField(upload_to='id_card/%Y/%m/%d/', blank=True)
    book_bank_photo = models.ImageField(upload_to='book_bank/%Y/%m/%d/', blank=True)
    bank_name = models.CharField(max_length=120, null=True, blank=True)
    bank_username = models.CharField(max_length=120, null=True, blank=True)
    bank_account_number = models.CharField(max_length=120, null=True, blank=True)
    register_created = models.DateTimeField(default=now)

    # # Boolean
    is_register = models.BooleanField(default=False, verbose_name='IS COMPLETE PERSONAL INFO')
    is_finished_regis = models.BooleanField(default=False, verbose_name='IS FINISHED REGISTRATION')
    is_approve = models.BooleanField(default=False, verbose_name='IS ADMIN APPROVE')
    is_already_approve = models.BooleanField(default=False)
    is_connect_bank = models.BooleanField(default=False, verbose_name='IS CONNECT TO BANK')

    # Refresh_data
    is_refresh_shouters_data = models.BooleanField(default=False, verbose_name='REFRESH SHOUTER DATA')

    # # Line Token
    line_access_token = models.CharField(max_length=1000, null=True, blank=True)
    line_access_token_updated = models.DateTimeField(default=now)
    line_id_token = models.CharField(max_length=1000, null=True, blank=True)
    line_id_token_updated = models.DateTimeField(default=now)

    # # Line User Information
    line_user_id = models.CharField(max_length=100, null=True, blank=True)
    line_username = models.CharField(max_length=100, null=True, blank=True)
    line_profile_picture = models.URLField(max_length=1000, null=True, blank=True)

    # # Raw Data
    ig_response_media_objects = models.JSONField(null=True, blank=True)
    ig_response_audience_insight = models.JSONField(null=True, blank=True)
    ig_response_active_follower = models.JSONField(null=True, blank=True)

    # # Facebook
    fb_main_access_token = models.CharField(max_length=1000, null=True, blank=True)
    fb_access_token_created = models.DateTimeField(default=now)
    fb_page_id = models.CharField(max_length=120, null=True, blank=True)
    fb_page_name = models.CharField(max_length=120, null=True, blank=True)
    fb_is_connect = models.BooleanField(default=False, verbose_name='IS CONNECT TO FACEBOOK PAGE')
    is_already_fb_connect = models.BooleanField(default=False)
    fb_name = models.CharField(max_length=500, null=True, blank=True)
    fb_profile_picture = models.URLField(max_length=1000, null=True, blank=True)

    # # Instagram
    ig_business_account_id = models.CharField(max_length=120, null=True, blank=True)
    ig_username = models.CharField(max_length=120, null=True, blank=True)
    ig_media_count = models.IntegerField(null=True, blank=True)
    ig_follower_count = models.IntegerField(null=True, blank=True)
    ig_following_count = models.IntegerField(null=True, blank=True)
    ig_active_follower = models.IntegerField(null=True, blank=True)
    ig_active_follower_harmonic = models.IntegerField(null=True, blank=True)
    ig_active_follower_percent = models.FloatField(null=True, blank=True)
    ig_profile_picture = models.URLField(max_length=1000, null=True, blank=True)

    # # Engagement
    ig_average_total_like = models.IntegerField(null=True, blank=True, verbose_name="IG => AVERAGE LIKE")
    ig_engagement_percent = models.FloatField(null=True, blank=True, verbose_name="IG => LIKE PERCENTAGE")
    ig_story_view = models.IntegerField(null=True, blank=True, verbose_name="IG => AVERAGE STORY VIEW")
    ig_average_post_reach = models.IntegerField(null=True, blank=True, verbose_name="IG => AVERAGE POST REACH")
    ig_predicted_ad_post_reach = models.IntegerField(null=True, blank=True, verbose_name="PREDICTED => AVERAGE POST REACH")
    ig_post_reach_guarantee = models.IntegerField(null=True, blank=True, verbose_name="GUARANTEE => POST REACH")
    ig_story_view_guarantee = models.IntegerField(null=True, blank=True, verbose_name="GUARANTEE => STORY VIEW")
    ig_ad_post_reach = models.IntegerField(null=True, blank=True, verbose_name="ESTIMATE => AD POST REACH")

    # # Pricing
    ig_price_story_fc = models.IntegerField(null=True, blank=True, verbose_name="IG STORY Price (MIN)")
    ig_price_story_ugc = models.IntegerField(null=True, blank=True, verbose_name="IG STORY Price (MAX)")
    ig_price_post_fc = models.IntegerField(null=True, blank=True, verbose_name="IG POST Price (MIN)")
    ig_price_post_ugc = models.IntegerField(null=True, blank=True, verbose_name="IG POST Price (MAX)")
    ig_price_story_post_fc = models.IntegerField(null=True, blank=True, verbose_name="IG STORY+POST Price (MIN)")
    ig_price_story_post_ugc = models.IntegerField(null=True, blank=True, verbose_name="IG STORY+POST Price (MAX)")

    ig_fb_price_story_fc = models.IntegerField(null=True, blank=True, verbose_name="IG+FB STORY Price (MIN)")
    ig_fb_price_story_ugc = models.IntegerField(null=True, blank=True, verbose_name="IG+FB STORY Price (MAX)")
    ig_fb_price_post_fc = models.IntegerField(null=True, blank=True, verbose_name="IG+FB POST Price (MIN)")
    ig_fb_price_post_ugc = models.IntegerField(null=True, blank=True, verbose_name="IG+FB POST Price (MAX)")
    ig_fb_price_story_post_fc = models.IntegerField(null=True, blank=True, verbose_name="IG+FB STORY+POST Price (MIN)")
    ig_fb_price_story_post_ugc = models.IntegerField(null=True, blank=True, verbose_name="IG+FB STORY+POST Price (MAX)")

    # # Work Selection
    is_check_ig = models.BooleanField(default=False, verbose_name="ACCEPT WORK (IG)")
    is_check_ig_fb = models.BooleanField(default=False, verbose_name="ACCEPT WORK (IG+FB)")
    is_check_ig_story = models.BooleanField(default=False, verbose_name="ACCEPT WORK (IG => STORY)")
    is_check_ig_post = models.BooleanField(default=False, verbose_name="ACCEPT WORK (IG => POST)")
    is_check_ig_story_post = models.BooleanField(default=False, verbose_name="ACCEPT WORK (IG => STORY + POST)")
    is_check_ig_fb_story = models.BooleanField(default=False, verbose_name="ACCEPT WORK (IG+FB => STORY)")
    is_check_ig_fb_post = models.BooleanField(default=False, verbose_name="ACCEPT WORK (IG+FB => POST)")
    is_check_ig_fb_story_post = models.BooleanField(default=False, verbose_name="ACCEPT WORK (IG+FB => STORY + POST)")

    is_check_tiktok = models.BooleanField(default=False, verbose_name="ACCEPT WORK (TIKTOK)")
    tiktok_name = models.CharField(max_length=120, null=True, blank=True, verbose_name="TIKTOK NAME")
    tiktok_price = models.IntegerField(null=True, blank=True, verbose_name="TIKTOK PRICE")
    is_check_twitter = models.BooleanField(default=False, verbose_name="ACCEPT WORK (TWITTER)")
    twitter_name = models.CharField(max_length=120, null=True, blank=True, verbose_name="TWITTER NAME")
    twitter_price = models.IntegerField(null=True, blank=True, verbose_name="TWITTER PRICE")

    # # Error
    is_error = models.BooleanField(default=False, verbose_name="SHOUTER IS ERROR")
    error_section = models.CharField(max_length=120, null=True, blank=True, verbose_name="ERROR SECTION")

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

    # def __str__(self):
    #     return self.first_name


# Function check before save
def shouters_pre_save(sender, instance, *args, **kwargs):
    # Admin Approve
    # if instance.is_approve is True and instance.is_already_approve is False:
    #     # Check IG PHOTO
    #     access_token = instance.fb_main_access_token
    #     business_account_id = instance.ig_business_account_id
    #     # Get Bio
    #     ig_profile_picture = ig_photo(business_account_id=business_account_id, access_token=access_token)
    #     instance.ig_profile_picture = ig_profile_picture
    #     instance.save()

    # Refresh Shouter Data
    if instance.is_refresh_shouters_data is True:
        # Get Init Data
        access_token = instance.fb_main_access_token
        business_account_id = instance.ig_business_account_id

        # Get New Data
        response = refresh_shouters(access_token=access_token, business_account_id=business_account_id)
        # FB Biography
        instance.fb_name = response.get("fb_name", None)
        instance.fb_profile_picture = response.get("fb_profile_picture", None)
        # IG Biography
        instance.ig_username = response.get("ig_username", None)
        instance.ig_media_count = response.get("ig_media_count", None)
        instance.ig_follower_count = response.get("ig_follower_count", None)
        instance.ig_following_count = response.get("ig_following_count", None)
        instance.ig_profile_picture = response.get("ig_profile_picture", None)
        # IG Active Follower
        instance.ig_response_active_follower = response.get("ig_response_active_follower", None)
        instance.ig_active_follower = response.get("ig_active_follower", None)
        instance.ig_active_follower_harmonic = response.get("ig_active_follower_harmonic", None)
        instance.ig_active_follower_percent = response.get("ig_active_follower_percent", None)
        # Media Objects
        instance.ig_response_media_objects = response.get("ig_response_media_objects", None)
        # Engagement
        instance.ig_average_total_like = response.get("ig_average_total_like", None)
        instance.ig_story_view = response.get("ig_story_view", None)
        instance.ig_average_post_reach = response.get("ig_average_post_reach", None)
        # Engagement => จากการคำนวน
        instance.ig_engagement_percent = response.get("ig_engagement_percent", None)
        instance.ig_predicted_ad_post_reach = response.get("ig_predicted_ad_post_reach", None)
        instance.ig_post_reach_guarantee = response.get("ig_post_reach_guarantee", None)
        instance.ig_story_view_guarantee = response.get("ig_story_view_guarantee", None)
        instance.ig_ad_post_reach = response.get("ig_ad_post_reach", None)
        # Price
        instance.ig_price_story_fc = response.get("ig_price_story_fc", None)
        instance.ig_price_story_ugc = response.get("ig_price_story_ugc", None)
        instance.ig_price_post_fc = response.get("ig_price_post_fc", None)
        instance.ig_price_post_ugc = response.get("ig_price_post_ugc", None)
        instance.ig_price_story_post_fc = response.get("ig_price_story_post_fc", None)
        instance.ig_price_story_post_ugc = response.get("ig_price_story_post_ugc", None)
        instance.ig_fb_price_story_fc = response.get("ig_fb_price_story_fc", None)
        instance.ig_fb_price_story_ugc = response.get("ig_fb_price_story_ugc", None)
        instance.ig_fb_price_post_fc = response.get("ig_fb_price_post_fc", None)
        instance.ig_fb_price_post_ugc = response.get("ig_fb_price_post_ugc", None)
        instance.ig_fb_price_story_post_fc = response.get("ig_fb_price_story_post_fc", None)
        instance.ig_fb_price_story_post_ugc = response.get("ig_fb_price_story_post_ugc", None)
        # Audience Insight
        instance.ig_response_audience_insight = response.get("ig_response_audience_insight",  None)
        # Save
        instance.is_refresh_shouters_data = False
        instance.save()


def shouters_post_save(sender, instance, *args, **kwargs):
    if instance.is_approve is True and instance.is_already_approve is False:
        instance.is_already_approve = True
        instance.save()

        # Sent Text and Flex Message
        # Get Init Data
        first_name = instance.first_name
        last_name = instance.last_name
        line_user_id = instance.line_user_id
        ig_username = instance.ig_username
        ig_profile_picture = instance.ig_profile_picture
        ig_follower_count = instance.ig_follower_count
        ig_follower_count = '{:,}'.format(ig_follower_count)

        response_text = api__admin_approve_text_message(line_user_id=line_user_id)
        response_flex = api__admin_approve_flex_message(line_user_id=line_user_id,
                                                        ig_profile_picture=ig_profile_picture,
                                                        first_name=first_name,
                                                        last_name=last_name,
                                                        ig_username=ig_username,
                                                        ig_follower_count=ig_follower_count)
        response_image = api__admin_approve_image_message(line_user_id=line_user_id)

# Run Pre and Post Save Function
pre_save.connect(shouters_pre_save, sender=Shouter)
post_save.connect(shouters_post_save, sender=Shouter)

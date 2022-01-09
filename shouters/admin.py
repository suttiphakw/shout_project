from django.contrib import admin
from shouters.models import Shouter

# Register your models here.
class ShouterAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'line_username', 'ig_username', 'ig_follower_count', 'is_register',
                    'fb_is_connect', 'is_approve')

    readonly_fields = (
        # Status
        'is_register', 'is_already_approve', 'is_already_fb_connect',
        # Personal Info
        'nickname', 'first_name', 'last_name', 'email', 'tel', 'gender',
        'birthday_date', 'birthday_month', 'birthday_year', 'province', 'education', 'college', 'interest',
        # Line
        'line_access_token', 'line_access_token_updated', 'line_id_token', 'line_id_token_updated', 'line_user_id',
        'line_username', 'line_profile_picture',
        # Facebook
        'fb_access_token', 'fb_access_token_created', 'fb_page_id', 'fb_is_connect',
        # Instagram
        'ig_business_account_id', 'ig_username', 'ig_media_count', 'ig_follower_count', 'ig_following_count',
        'ig_active_follower', 'ig_active_follower_harmonic', 'ig_active_follower_percent', 'ig_estimated_reach',
        'ig_profile_picture', 'ig_total_like', 'ig_average_total_like', 'ig_engagement_percent', 'ig_story_view',
        'ig_average_post_reach', 'ig_predicted_ad_post_reach', 'ig_ad_post_reach',
        # Pricing
        'ig_price_story_fc', 'ig_price_story_ugc', 'ig_price_post_fc', 'ig_price_post_ugc', 'ig_price_story_post_fc',
        'ig_price_story_post_ugc',
        'ig_fb_price_story_fc', 'ig_fb_price_story_ugc', 'ig_fb_price_post_fc', 'ig_fb_price_post_ugc',
        'ig_fb_price_story_post_fc', 'ig_fb_price_story_post_ugc',
        # Work Selection
        'is_check_ig', 'is_check_ig_story', 'is_check_ig_post', 'is_check_ig_story_post',
        'is_check_ig_fb', 'is_check_ig_fb_story', 'is_check_ig_fb_post', 'is_check_ig_fb_story_post',
        'is_check_tiktok', 'tiktok_name', 'tiktok_price',
        'is_check_twitter', 'twitter_name', 'twitter_price',
        # RawData
        'fb_response_access_token', 'fb_response_page_id', 'fb_response_business_account_id', 'ig_response_bio',
        'ig_response_media_objects', 'ig_response_audience_insight', 'ig_response_active_follower',
    )

    fieldsets = (
        ('Status', {'fields': ('is_approve', 'is_register', 'fb_is_connect')}),
        ('Personal Info', {'fields': ('nickname', 'first_name', 'last_name', 'email', 'tel', 'gender',
                                      'birthday_date', 'birthday_month', 'birthday_year', 'province', 'education',
                                      'college', 'interest',)}),
        ('Pricing', {'fields': ('ig_price_story_fc', 'ig_price_story_ugc', 'ig_price_post_fc', 'ig_price_post_ugc',
                                'ig_price_story_post_fc', 'ig_price_story_post_ugc', 'ig_fb_price_story_fc',
                                'ig_fb_price_story_ugc', 'ig_fb_price_post_fc', 'ig_fb_price_post_ugc',
                                'ig_fb_price_story_post_fc', 'ig_fb_price_story_post_ugc',)}),
        ('Line User Info', {'fields': ('line_username', 'line_profile_picture')}),
        ('Instagram User Info', {'fields': ('ig_username', 'ig_media_count', 'ig_follower_count', 'ig_following_count',
                                            'ig_active_follower',
                                            'ig_active_follower_percent', 'ig_estimated_reach', 'ig_profile_picture',
                                            'ig_total_like', 'ig_average_total_like', 'ig_engagement_percent',
                                            'ig_story_view', 'ig_average_post_reach', 'ig_predicted_ad_post_reach',
                                            'ig_ad_post_reach',)}),
        ('Work Selection', {'fields': ('is_check_ig', 'is_check_ig_story', 'is_check_ig_post', 'is_check_ig_story_post',
                                       'is_check_ig_fb', 'is_check_ig_fb_story', 'is_check_ig_fb_post',
                                       'is_check_ig_fb_story_post', 'is_check_tiktok', 'tiktok_name', 'tiktok_price',
                                       'is_check_twitter', 'twitter_name', 'twitter_price',)}),
        ('Line Token Info', {'fields': ('line_user_id', 'line_access_token', 'line_access_token_updated',
                                        'line_id_token', 'line_id_token_updated')}),
        ('Facebook Token Info', {'fields': ('fb_access_token', 'fb_access_token_created', 'fb_page_id',
                                            )}),
        ('Raw Data', {'fields': ('fb_response_access_token', 'fb_response_page_id', 'fb_response_business_account_id',
                                 'ig_response_bio', 'ig_response_media_objects', 'ig_response_audience_insight',
                                 'ig_response_active_follower',)}),
    )

admin.site.register(Shouter, ShouterAdmin)
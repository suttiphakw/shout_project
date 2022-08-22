from django.contrib import admin
from .models import Campaign

# Register your models here.
# class CampaignAdmin(admin.ModelAdmin):
#   readonly_fields = ('campaign_created',)
#   fieldsets = (
#     ('Status', {'fields': ('user', 'campaign_created',)}),
#     ('Campaign Info', {'fields': ('campaign_name', 'campaign_is_ig', 'campaign_is_fb', 'campaign_is_tiktok', 'campaign_is_twitter',
#                                   'campaign_budget', 'campaign_work_type', 'campaign_content_type_story', 'campaign_content_type_post')}),
#     ('Campaign Result', {'fields': ('cal_number_shouter_min', 'cal_number_shouter_max', 'cal_estimate_reach_min', 'cal_estimate_reach_max',
#                                     'cal_cpr_min', 'cal_cpr_max',)}),
#   )
# admin.site.register(Campaign, CampaignAdmin)


# Register your models here.
class CampaignAdmin(admin.ModelAdmin):
  pass


admin.site.register(Campaign, CampaignAdmin)
from django.contrib import admin
from .models import BrandProfile

# Register your models here.
class BrandAdmin(admin.ModelAdmin):
  pass
admin.site.register(BrandProfile, BrandAdmin)

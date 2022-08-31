from django.contrib import admin
from .models import Order


# Register your models here.
class OrderAdmin(admin.ModelAdmin):
  list_display = ['__str__', 'is_selected']
  search_fields = ['id']


admin.site.register(Order, OrderAdmin)
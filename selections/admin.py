from django.contrib import admin
from selections.models import Selection


# Register your models here.
class SelectionAdmin(admin.ModelAdmin):
  pass


admin.site.register(Selection, SelectionAdmin)
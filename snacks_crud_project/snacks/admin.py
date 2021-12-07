from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from .models import Snack

# Register your models here.

class AdminSnack(admin.ModelAdmin):
  list_display = ['title', 'description', 'rate', 'purchaser']
  search_fields = ['title',]
  list_display_links = ('title', 'purchaser',)
  list_filter = ['purchaser']

admin.site.register(Snack, AdminSnack)

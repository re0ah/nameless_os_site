from django.contrib import admin
from .models import Bug

@admin.register(Bug)
class BugAdmin(admin.ModelAdmin):
	list_display = [i.name for i in Bug._meta.fields]

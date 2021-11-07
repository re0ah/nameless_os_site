from django.contrib import admin
from .models import Bug, Bug_type

@admin.register(Bug)
class BugAdmin(admin.ModelAdmin):
	list_display = [i.name for i in Bug._meta.fields]

@admin.register(Bug_type)
class BugTypeAdmin(admin.ModelAdmin):
	list_display = [i.name for i in Bug_type._meta.fields]

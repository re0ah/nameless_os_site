from django.contrib import admin
from .models import Page

@admin.register(Page)
class CategoryAdmin(admin.ModelAdmin):
	list_display = [i.name for i in Page._meta.fields]
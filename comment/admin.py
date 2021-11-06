from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = [i.name for i in Comment._meta.fields]

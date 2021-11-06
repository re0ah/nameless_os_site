from django.contrib import admin
from .models import Task, Task_type

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
	list_display = [i.name for i in Task._meta.fields]

@admin.register(Task_type)
class TaskTypeAdmin(admin.ModelAdmin):
	list_display = [i.name for i in Task_type._meta.fields]

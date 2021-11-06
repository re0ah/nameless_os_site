from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Program

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
	list_display = [i.name for i in Program._meta.fields]

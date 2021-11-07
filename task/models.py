from django.db import models
import datetime
from django.contrib.auth.models import User

class Task_type(models.Model):
	class Meta:
		verbose_name_plural = "Тип задачи"
	title	= models.CharField(max_length=64, default="Задача", blank=True)

	def __str__(self):
		return f'{self.title}'

class Task(models.Model):
	class Meta:
		verbose_name_plural = "Задача"
	active			= models.BooleanField(blank=False)
	title			= models.CharField(max_length=64, verbose_name='Название задачи', default="Задача", blank=True)
	content			= models.TextField(verbose_name='Содержание', blank=True)
	date_create		= models.DateTimeField(default=datetime.datetime.now)
	date_resolve	= models.DateTimeField(null=True, blank=True)
	author			= models.ForeignKey(User, on_delete=models.CASCADE)
	task_type		= models.ForeignKey(Task_type, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.title}'


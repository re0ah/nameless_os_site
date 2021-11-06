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
	active		= models.BooleanField(blank=False)
	content		= models.TextField(verbose_name='Содержание', blank=True)
	date		= models.DateField(default=datetime.date.today)
	author		= models.ForeignKey(User, on_delete=models.CASCADE)
	task_type	= models.ForeignKey(Task_type, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.title}'


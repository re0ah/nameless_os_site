from django.db import models
import datetime

class Program(models.Model):
	class Meta:
		verbose_name_plural = "Программа"
	active			= models.BooleanField(blank=True)
	title			= models.CharField(max_length=64, verbose_name='Название программы', default="Название программы", blank=True)
	date_publicate	= models.DateField(default=datetime.date.today)
	date_create		= models.DateField(default=datetime.date.today)
	source			= models.URLField(blank=False, default="https://github.com/re0ah/nameless-OS16")
	file			= models.FileField(blank=False)

	def __str__(self):
		return f'{self.title}'

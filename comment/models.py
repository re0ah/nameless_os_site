from django.db import models
import datetime
from django.contrib.auth.models import User

class Comment(models.Model):
	class Meta:
		verbose_name_plural = "Комментарий"
	active	= models.BooleanField(blank=False)
	content	= models.TextField(verbose_name='Содержание', blank=True)
	date	= models.DateField(default=datetime.date.today)
	author	= models.ForeignKey(User, on_delete=models.CASCADE)
	answer	= models.ForeignKey("self", on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.title}'

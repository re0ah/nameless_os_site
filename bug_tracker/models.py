from django.db import models
import datetime
from django.contrib.auth.models import User
from comment.models import Comment

class Bug(models.Model):
	class Meta:
		verbose_name_plural = "Ошибка"
	active			= models.BooleanField(blank=False)
	title			= models.CharField(max_length=64, verbose_name='Название ошибки', default="Ошибка", blank=True)
	content			= models.TextField(verbose_name='Содержание', blank=True)
	date_create 	= models.DateField(default=datetime.date.today)
	date_resolve	= models.DateField(blank=True)
	comments		= models.ManyToManyField(Comment, symmetrical=False, null=True, blank=True, related_name='+')
	author			= models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.title}'


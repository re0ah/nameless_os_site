from django.db import models
import datetime
from django.contrib.auth.models import User
from comment.models import Comment

class Bug_type(models.Model):
	class Meta:
		verbose_name_plural = "Тип ошибки"

	title = models.CharField(max_length=64, verbose_name='Тип ошибки', default="Ошибка", blank=True)

	def __str__(self):
		return f'{self.title}'

class Bug(models.Model):
	class Meta:
		verbose_name_plural = "Ошибка"
	active			= models.BooleanField(blank=False)
	title			= models.CharField(max_length=64, verbose_name='Название ошибки', default="Ошибка", blank=True)
	content			= models.TextField(verbose_name='Содержание', blank=True)
	date_create 	= models.DateTimeField(default=datetime.datetime.now)
	date_resolve	= models.DateTimeField(null=True, blank=True)
	comments		= models.ManyToManyField(Comment, symmetrical=False, null=True, blank=True, related_name='+')
	bug_type		= models.ForeignKey(Bug_type, null=True, on_delete=models.CASCADE)
	author			= models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.title}'


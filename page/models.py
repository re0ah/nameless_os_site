from django.db import models
import datetime

class Page(models.Model):
	class Meta:
		verbose_name_plural = "Страница"
	active		= models.BooleanField(blank=False)
	title		= models.CharField(max_length=64, verbose_name='Название страницы', default="Страница", blank=True)
	content		= models.TextField(verbose_name='Содержание страницы', blank=True)
	date_change	= models.DateField(default=datetime.date.today)
	master_page = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
	slave_pages = models.ManyToManyField("self", symmetrical=False, null=True, blank=True, related_name='+')

	def __str__(self):
		return f'{self.title}'


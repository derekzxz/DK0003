from django.db import models
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe


class Category(models.Model):
	name = models.CharField(max_length=200)
	slug = models.SlugField(max_length=220)
	publish = models.BooleanField(default=True)
	profile = models.TextField(null=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "categories"

	def get_absolute_url(self):
		return reverse('post:category', args=[self.slug])


class Post(models.Model):
	category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	body = models.TextField()
	publish = models.BooleanField(default=True)
	slug = models.SlugField(max_length=220)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post:detail', args=[self.slug])

	def display_my_safefield(self):
		return mark_safe(self.body)


class Book(models.Model):
	title = models.CharField(max_length=200)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	def __str__(self):
		return self.title


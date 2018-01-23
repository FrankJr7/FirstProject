from django.db import models

class Image(models.Model):
	file = models.ImageField(upload_to='static/', default='no-img.jpg')
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=200)

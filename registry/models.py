from django.db import models

class Link(models.Model):
	logo_url = models.ImageField(upload_to='registry')
	name = models.TextField()
	url = models.URLField()

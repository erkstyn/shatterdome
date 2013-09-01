from django.db import models

class Entry(models.Model):
	name = models.CharField(max_length=255)
	comment = models.TextField()
	email = models.EmailField(null=True, blank=True)
	image = models.ImageField(null=True, blank=True, upload_to='entries')
	
	class Meta:
		verbose_name_plural = 'entries'
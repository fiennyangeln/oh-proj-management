from django.db import models

# Create your models here.

class Project(models.Model):
	id_ = models.IntegerField(primary_key=True)
	basename = models.TextField()
	created = models.DateField()
	download_url = models.TextField()
	complete = models.BooleanField(default=False)
	dataYear = models.IntegerField()
	description = models.TextField()
	metadata = models.TextField() # in json
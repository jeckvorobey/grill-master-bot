from django.db import models

from utils.models import CreateUpdateTracker


class Category(CreateUpdateTracker):
	id = models.BigAutoField(primary_key=True)
	name = models.CharField(max_length=255)
	label = models.CharField(max_length=255)
	
	def __str__(self):
		return self.label


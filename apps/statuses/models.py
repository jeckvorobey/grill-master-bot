from django.db import models

from utils.models import CreateUpdateTracker


class Status(CreateUpdateTracker):
	id = models.BigAutoField(primary_key=True)
	name = models.CharField(max_length=100)
	label = models.CharField(max_length=100)
	
	def __str__(self):
		return self.label

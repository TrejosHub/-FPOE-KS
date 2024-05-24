from django.db import models

class Silla(models.Model):
	material 			= models.TextField(max_length=5000, null=False, blank=True)
	altura 				= models.FloatField(max_length=5000, null=False, blank=True)
	peso 				= models.FloatField(max_length=5000, null=False, blank=True)
	estilo 				= models.TextField(max_length=5000, null=False, blank=True)
	def __str__(self):
		return self.material
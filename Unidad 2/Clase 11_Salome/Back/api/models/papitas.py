from django.db import models
	
class Papitas(models.Model):
	marca 				= models.TextField(max_length=50, null=False, blank=True)
	sabor 				= models.TextField(max_length=5000, null=False, blank=True)
	color 		= models.TextField(max_length=5000, null=False, blank=True)
	cantidad 		= models.IntegerField(null=False)
	def __str__(self):
		return self.marca
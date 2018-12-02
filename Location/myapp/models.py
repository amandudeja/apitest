from django.db import models

# Create your models here.

class Location(models.Model):
	key 		= models.CharField(max_length = 20)
	place_name 	= models.CharField(max_length = 50)
	admin_name 	= models.CharField(max_length = 50)
	latitude 	= models.FloatField(max_length = 10)
	longitude 	= models.FloatField(max_length = 10)



	def __str__(self):
		return self.key
	


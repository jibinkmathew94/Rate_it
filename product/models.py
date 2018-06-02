from django.db import models
from company.models import Company

# Create your models here.


class Catogory(models.Model):
	name = models.CharField(max_length=120, null=False, blank=False)

	def __str__(self):
		return self.name



class Product(models.Model):
	
	name		= models.CharField(max_length=120, null=False, blank=False)
	company		= models.ForeignKey(Company,on_delete=models.CASCADE)
	catogory	= models.ForeignKey(Catogory,on_delete=models.CASCADE)
	description = models.CharField(max_length=120)

	def __str__(self):
			return self.name
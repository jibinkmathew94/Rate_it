from django.db import models
from product.models import Product

# Create your models here.

class Review(models.Model):

	comment		= models.CharField(max_length=120)
	product		= models.ForeignKey(Product,on_delete=models.CASCADE)
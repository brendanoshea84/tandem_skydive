from django.db import models
from datetime import datetime 


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


        
# Create your models here.
class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    

    def __str__(self):
        return self.name

class Jumper(models.Model):
    jumper_Name = models.CharField(max_length=254, null=False, blank=False)
    Phone_Number = models.CharField(max_length=20, null=True, blank=True)
    Email = models.EmailField(max_length=40, null=False, blank=False, default="")

     

    def __str__(self):
        return self.name      
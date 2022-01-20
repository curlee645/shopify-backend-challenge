from django.db import models

# Create your models here.
class Inventory(models.Model):
    purchaseId = models.AutoField(primary_key = True)
    productName = models.CharField(max_length = 500)
    purchaseDate = models.DateField()
    supplier = models.CharField(max_length = 500)
    productQuantity = models.IntegerField()
    costPerUnit = models.DecimalField(decimal_places = 2, max_digits=10)
    purchaseAmount = models.DecimalField(decimal_places = 2, max_digits=10)
    

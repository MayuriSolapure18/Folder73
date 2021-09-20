from django.db import models



class Product(models.Model):
    Date = models.DateField()
    Provider = models.CharField(max_length=50)
    Name_of_product = models.CharField(max_length=50)
    Price = models.IntegerField()
    Quantity = models.IntegerField()
    Amount = models.IntegerField()
    Stock = models.IntegerField()


    def __str__(self):
        return self.Name_of_product

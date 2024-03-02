from django.db import models

class product(models.Model):
  Product_ID=models.CharField(max_length=255)
  name = models.CharField(max_length=255)
  image = models.CharField(max_length=255, default="No Inage available")
  leftInStock = models.IntegerField(null=True)
  stock_date = models.DateField(null=True)

  def __str__(self):
    return self.name

class order(models.Model):
  Order_ID=models.CharField(max_length=255)
  Product_ID=models.ForeignKey(product, on_delete=models.CASCADE)
  customer_email = models.CharField(max_length=255)
  order_date = models.DateField(null=True)
  
  def __str__(self):
    return self.Order_ID

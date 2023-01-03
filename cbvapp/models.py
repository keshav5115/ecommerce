from django.db import models
from products.models import Product
from customer.models import Customer
# Create your models here.
class Orders(models.Model):
    orderid=models.AutoField(primary_key=True)
    date_of_order=models.DateField(auto_now_add=True)
    quantity=models.IntegerField()
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)

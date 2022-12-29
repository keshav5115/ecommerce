from django.db import models

# Create your models here.

    

class Product(models.Model):
    product_name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField()
    product_image=models.ImageField(upload_to='img')

    def __str__(self):
        return self.product_name
    
class Review(models.Model):
    text=models.TextField()
    list=[['1','1'],['2','2'],['3','3'],['4','4'],['5','5']]
    rating=models.CharField(max_length=5,choices=list,default='3')
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    





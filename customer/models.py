from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(User):
    mobile=models.PositiveBigIntegerField()
    gen=[['male','male'],['female','female']]
    gender=models.CharField(max_length=10,choices=gen)

    def __str__(self):
        return self.username
    
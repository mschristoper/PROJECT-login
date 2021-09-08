from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=200 , null=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    userName = models.CharField(max_length=200 , null=True)
    firstName = models.CharField(max_length=200, null=True)
    lastName = models.CharField(max_length=200,null=True)
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200,null =True)
    email = models.CharField(max_length=200, null=True, unique= True)
    birthday = models.DateTimeField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
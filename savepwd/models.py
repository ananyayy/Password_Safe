from django.db import models

# Create your models here.


class Pwd(models.Model):

   sname = models.CharField(max_length = 255)
   paswd =  models.CharField(max_length = 255)

class Customer(models.Model):
    ans = models.CharField(max_length=255)
    eml = models.EmailField(default="abc@email.com")
    
    
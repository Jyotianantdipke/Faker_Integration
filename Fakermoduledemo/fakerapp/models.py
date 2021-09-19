from django.db import models

# Create your models here.

class Studentdata(models.Model):
    Name=models.CharField(max_length=64)
    Address=models.CharField(max_length=256)
    Email=models.EmailField(max_length=32)
    Company=models.CharField(max_length=32,default=None)



    def __str__(self):
        return f'{self.Name} {self.Address},{self.Company}'
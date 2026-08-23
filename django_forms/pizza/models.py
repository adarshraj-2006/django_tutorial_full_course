from django.db import models

# Create your models here.
class SizePizza(models.Model):
    title=models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Pizza(models.Model):
    topping1=models.CharField(max_length=100)
    topping2=models.CharField(max_length=100)
    size=models.ForeignKey(SizePizza,on_delete=models.CASCADE)

from django.db import models

# Create your models here.


class Pizza(models.Model):
    '''Defining a pizza.'''
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Topping(models.Model):
    '''Defining a topping.'''
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

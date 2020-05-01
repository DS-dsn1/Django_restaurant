from django.db import models
from django.utils import timezone


# Create your models here.
class Chef(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    experience = models.CharField(max_length=250)
    salary = models.FloatField(max_length=50)

    def __str__(self):
        return f'Chef {self.id}: {self.first_name} {self.last_name}'


class Dish(models.Model):
    name = models.CharField(max_length=250)
    recipe = models.TextField()
    ingredients = models.CharField(max_length=250)
    cost = models.FloatField(max_length=30)
    chefs = models.ManyToManyField(Chef)


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.id}: {self.first_name} {self.last_name}'


class Orders(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateTimeField(default=timezone.now)
    dishes = models.ManyToManyField(Dish)


class Payment(models.Model):
    PAYMENT_CHOICES = (
        ('cash', 'Cash payment'),
        ('card', 'Credit card payment'),
        ('apple', 'Payment via Apple Pay')
    )
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=10,
                                      choices=PAYMENT_CHOICES,
                                      default='cash')


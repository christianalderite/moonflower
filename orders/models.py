from django.db import models
from datetime import datetime
from django.conf import settings

class Payments(models.Model):
    title = models.CharField(blank=True, max_length=150)
# Create your models here.

class OrderManager(models.Manager):
    def create_order(self, title):
        order = self.create(title=title)
        return order

class Order(models.Model):
    created_on = models.DateField(default=datetime.now())
    title = models.CharField(blank=True, max_length=150)
    updated_on = models.DateField(auto_now_add=True)
    payment_id = models.ForeignKey(Payments, on_delete=models.CASCADE)
    value = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    discount = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    final_value = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    is_paid = models.BooleanField(default=True)
    objects = models.Manager()
    browser = OrderManager()

class Products(models.Model):
    created_on = models.DateField(default=datetime.now())
    name = models.CharField(blank=True, max_length=255)
    updated_on = models.DateField(auto_now_add=True)
    price = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    discount = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    quantity = models.IntegerField(default=0)


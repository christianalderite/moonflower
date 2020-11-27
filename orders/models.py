from django.db import models
from datetime import datetime
from django.conf import settings
# Create your models here.

class OrderManager(models.Manager):
    def create_order(self, title):
        order = self.create(title=title)
        return order

class Order(models.Model):
    created_on = models.DateField(default=datetime.now())
    title = models.CharField(blank=True, max_length=150)
    updated_on = models.DateField(auto_now_add=True)
    value = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    discount = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    final_value = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    is_paid = models.BooleanField(default=True)
    objects = models.Manager()
    browser = OrderManager()

class Payment(models.Model):
    title = models.CharField(blank=True, max_length=150)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)

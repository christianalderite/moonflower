from django.db import models
from datetime import datetime
from django.conf import settings

CURRENCY = settings.CURRENCY

# Create your models here.
class OrderManager(models.Manager):
    def create_order(self, title):
        order = self.create(title=title)
        return order

class Order(models.Model):
    date = models.DateField(default=datetime.now())
    title = models.CharField(blank=True, max_length=150)
    timestamp = models.DateField(auto_now_add=True)
    value = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    discount = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    final_value = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    is_paid = models.BooleanField(default=True)
    objects = models.Manager()
    browser = OrderManager()


book = Book.objects.create_book("Pride and Prejudice")
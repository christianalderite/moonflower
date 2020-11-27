from django.db import models
from django.urls import reverse
from datetime import datetime
from django.conf import settings

# Create your models here.
class Product(models.Model):
    created_on = models.DateField(default=datetime.now())
    name = models.CharField(blank=True, max_length=255)
    updated_on = models.DateField(auto_now_add=True)
    price = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    discount = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('edit', kwargs={'pk': self.pk})
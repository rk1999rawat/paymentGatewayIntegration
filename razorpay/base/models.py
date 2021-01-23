from django.db import models

# Create your models here.

class Donations(models.Model):
    name = models.CharField(max_length=1000 , blank=True)
    email = models.EmailField(max_length=100, blank=True)
    amount = models.CharField(max_length=100, blank=True)
    order_id = models.CharField(max_length=1000)
    razorpay_payment_id = models.CharField(max_length=1000, blank=True)
    paid = models.BooleanField(default=False)

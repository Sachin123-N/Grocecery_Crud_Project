from django.db import models


class Grocesory(models.Model):
    PAYMENT_MODE = [('ON', 'ONLINE PAYMENT'), ("EMI", "MONTHLY INSTALLMENT")]
    shop_name = models.CharField(max_length=20)
    total_price = models.IntegerField()
    flat_no = models.IntegerField()
    discout_price = models.IntegerField()
    payment_mode = models.CharField(max_length=10, choices=PAYMENT_MODE)





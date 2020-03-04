from django.db import models

class Customer(models.Model):
    YES = 'Y'
    NO = 'N'
    ACTIVE_CHOICES = [
        (YES, 'Yes'),
        (NO, 'No'),
    ]
    name = models.CharField(max_length=255)
    account = models.SlugField(max_length=255)
    active = models.CharField(max_length=2,choices=ACTIVE_CHOICES,default=YES)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "customer"


class Order(models.Model):
    order_number = models.CharField(max_length=255)
    customer_order_number = models.SlugField(max_length=255)
    delivery_postcode = models.CharField(max_length=255)
    order_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "order"
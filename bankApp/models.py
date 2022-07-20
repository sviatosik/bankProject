from django.db import models


# Create your models here.


class Client(models.Model):
    client_name = models.CharField(max_length=40)
    client_thirname = models.CharField(max_length=40)
    client_age = models.CharField(max_length=40, default=0)
    cart_number = models.IntegerField(null=True)
    cart_balance = models.IntegerField(default=0)

    def __str__(self):
        return self.client_name, self.client_thirname, self.cart_balance, self.cart_number, self.client_age

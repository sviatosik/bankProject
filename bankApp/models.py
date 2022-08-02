from django.db import models


# Create your models here.
class Bank(models.Model):
    bank_name = models.CharField(max_length=100)
    bank_email = models.EmailField()

    def __str__(self):
        return f'{self.bank_name}'

class Client(models.Model):
    USD = 'USD'
    EUR = 'EUR'
    UKR = 'UKR'
    CARRENCY_CHOICES = [(USD, 'dollar'),
                        (EUR, 'euro'),
                        (UKR, 'grivnia')]
    client_name = models.CharField(max_length=40)
    client_thirname = models.CharField(max_length=40)
    client_age = models.CharField(max_length=40, default=0)
    client_gender = models.CharField(max_length=40, default="NONE")
    cart_number = models.IntegerField(null=True)
    cart_balance = models.IntegerField(default=0)
    carrancy = models.CharField(max_length=3, choices=CARRENCY_CHOICES, default='USD')
    bank = models.ForeignKey(Bank, on_delete=models.PROTECT, null=True)
    #
    # def __str__(self):
    #     return f'{self.client_name},{self.client_thirname},{self.cart_balance},{self.cart_number},' \
    #            f' {self.client_age}'

    def __str__(self):
        return f'{self.client_name}, {self.client_thirname}'

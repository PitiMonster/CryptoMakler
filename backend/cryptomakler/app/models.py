from django.db import models


class User(models.Model):
    ROLE_CHOICES = [
        'INV', 'Investor',
        'BRK', 'Broker'
    ]

    username = models.CharField(unique=True, max_length=32)
    createdAt = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=3, choices=ROLE_CHOICES)
    password = models.CharField(max_length=64)
    email = models.EmailField(max_length=32)

    def __str__(self):
        return self.username


class Fund(models.Model):
    name = models.CharField(max_length=32)
    broker = models.ForeignKey(User)
    total_value = models.FloatField()
    fee = models.FloatField()

    def __str__(self) -> str:
        return self.name


class Investment(models.Model):
    fund = models.ForeignKey(Fund)
    investor = models.ForeignKey(User)
    share_amount = models.FloatField()

    def __str__(self) -> str:
        return f'Investment of {self.investor} in {self.fund}'


class Coin(models.Model):
    api_id = models.CharField(max_length=64)
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Asset(models.models):
    fund = models.ForeignKey(Fund)
    coin = models.ForeignKey(Coin)
    coin_amount = models.FloatField()

    def __str__(self) -> str:
        return f'Asset: {self.coin} of {self.fund}'

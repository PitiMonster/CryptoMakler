from django.db import models
from django.contrib.auth.models import User


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
    initial_value = models.FloatField()

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


class Invitation(models.Model):
    sender = models.ForeignKey(User)
    receiver = models.ForeignKey(User)
    fund = models.ForeignKey(Fund)

    def __str__(self) -> str:
        return f'Invitation from {self.sender} to {self.receiver} to fund: {self.fund} '

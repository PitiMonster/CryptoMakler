from django.db import models
from django.contrib.auth.models import User


class Fund(models.Model):
    name = models.CharField(max_length=32)
    broker = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    total_value = models.FloatField()
    fee = models.FloatField()

    def __str__(self) -> str:
        return f'{self.name}'


class Investment(models.Model):
    fund = models.ForeignKey(Fund, on_delete=models.DO_NOTHING, related_name='investments')
    investor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    share_amount = models.FloatField()
    initial_value = models.FloatField()

    def __str__(self) -> str:
        return f'Investment({self.pk}) of {self.investor} in {self.fund}({self.fund.pk})'


class Coin(models.Model):
    api_id = models.CharField(max_length=64)
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Asset(models.Model):
    fund = models.ForeignKey(Fund, on_delete=models.CASCADE)
    coin = models.ForeignKey(Coin, on_delete=models.DO_NOTHING)
    coin_amount = models.FloatField()

    def __str__(self) -> str:
        return f'Asset: {self.coin} of {self.fund}'


class Invitation(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_invitations')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_invitations')
    fund = models.ForeignKey(Fund, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Invitation from {self.sender} to {self.receiver} to fund: {self.fund} '

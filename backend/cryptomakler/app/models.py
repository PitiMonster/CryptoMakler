from django.db import models
from django.contrib.auth.models import User

from .utils import throw_if_unvalid_amount

import random


class Fund(models.Model):
    name = models.CharField(max_length=32)
    broker = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    total_value = models.FloatField()
    fee = models.FloatField()

    def calculate_total_price(self):
        total_price = 0
        for asset in self.assets.iterator():
            total_price += asset.calculate_total_price()
        return total_price

    def calculate_share_price(self):
        if self.total_value == 0:
            return 1.0
        total_price = self.calculate_total_price()
        share_price = total_price / self.total_value
        return share_price

    def remove_share_amount(self, share_amount_diff):
        throw_if_unvalid_amount(share_amount_diff)

        if self.total_value < share_amount_diff:
            raise Exception('Fund does not have enough shares!')

        percentage = share_amount_diff / self.total_value

        for asset in self.assets.iterator():
            asset.coin_amount *= 1 - percentage
            asset.save()

        self.total_value -= share_amount_diff
        self.save()

    def add_share_amount(self, fiat_amount: float, share_amount_diff: float):
        throw_if_unvalid_amount(share_amount_diff)

        for asset in self.assets.iterator():
            coin_price = asset.coin.get_price()
            budget = fiat_amount * asset.fund_percent / 100.0
            coin_amount_diff = budget / coin_price
            asset.coin_amount += coin_amount_diff
            asset.save()

        self.total_value += share_amount_diff
        self.save()

    def __str__(self) -> str:
        return f'{self.name}'


class Investment(models.Model):
    fund = models.ForeignKey(
        Fund, on_delete=models.DO_NOTHING, related_name='investments')
    investor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    share_amount = models.FloatField(default=0)
    initial_value = models.FloatField(default=0)

    def add_share_amount(self, fiat_amount: float, share_amount_diff: float):
        throw_if_unvalid_amount(fiat_amount)
        throw_if_unvalid_amount(share_amount_diff)

        self.share_amount += share_amount_diff
        self.initial_value += fiat_amount

        self.fund.add_share_amount(fiat_amount=fiat_amount, share_amount_diff=share_amount_diff)
        self.save()

    def remove_share_amount(self, share_amount_diff):
        throw_if_unvalid_amount(share_amount_diff)

        if self.share_amount < share_amount_diff:
            raise Exception('Investor does not have enough funds!')

        if share_amount_diff == self.share_amount:
            self.initial_value = 0
            self.share_amount = 0
        else:
            self.initial_value -= self.initial_value * share_amount_diff / self.share_amount
            self.share_amount -= share_amount_diff

        self.fund.remove_share_amount(share_amount_diff)
        self.save()

    def __str__(self) -> str:
        return f'Investment({self.pk}) of {self.investor} in {self.fund}({self.fund.pk})'


class Coin(models.Model):
    api_id = models.CharField(max_length=64)
    name = models.CharField(max_length=32)

    def get_price(self):
        if "APIClient" not in dir():
            from .apps import APIClient
        coin_price = APIClient.getCoinPrice(self)
        return coin_price

    def __str__(self):
        return self.name + ' ' + str(self.id)


class Asset(models.Model):
    fund = models.ForeignKey(Fund, on_delete=models.CASCADE, related_name='assets')
    coin = models.ForeignKey(Coin, on_delete=models.DO_NOTHING)
    coin_amount = models.FloatField(default=0)
    fund_percent = models.FloatField(default=0)

    def calculate_total_price(self):
        coin_price = self.coin.get_price()
        asset_price = self.coin_amount * coin_price
        return asset_price

    def __str__(self) -> str:
        return f'Asset: {self.coin} of {self.fund}; id={self.id}'


class Invitation(models.Model):
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='sent_invitations')
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='received_invitations')
    fund = models.ForeignKey(Fund, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Invitation from {self.sender} to {self.receiver} to fund: {self.fund} '


class FakeAPI(models.Model):

    def __init__(self, *args, **kwargs):
        print('init api')

    def getCoinPrice(self, coin) -> float:
        if coin.name == 'BTC':
            return 2.0
        else:
            return 1.0
        # return random.random() * 1000

from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('INV', 'Investor'),
        ('BRK', 'Broker')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=3, choices=ROLE_CHOICES, default='INV')

    def __str__(self):
        return f'{self.user}({self.role})'

from django.contrib import admin
from .models import Fund, Investment, Coin, Asset, Invitation

admin.site.register(Fund)
admin.site.register(Investment)
admin.site.register(Coin)
admin.site.register(Asset)
admin.site.register(Invitation)

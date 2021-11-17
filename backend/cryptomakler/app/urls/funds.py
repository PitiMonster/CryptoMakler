from django.urls import path

urlpatterns = [
    path('', lambda:''),  # get all funds / post - create fund
    path(':id', lambda:''),  # get specific fund / del - remove fund
    # del - remove investment / patch - edit investment data
    path(':id/investment/:investmentId', lambda:''),
]

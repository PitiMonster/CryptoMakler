from django.urls import path

urlpatterns = [
    path(''),  # get all funds / post - create fund
    path(':id'),  # get specific fund / del - remove fund
    # del - remove investment / patch - edit investment data
    path(':id/investment/:investmentId'),
]

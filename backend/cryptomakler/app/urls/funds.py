from django.urls import path

urlpatterns = [
    path('/'),  # get all funds / post - create fund
    path('/:id'),  # get specific fund / del - remove fund
    path('/:id/investors'),  # get all investors
    path('/:id/investors/:id'),  # del - remove investor
]

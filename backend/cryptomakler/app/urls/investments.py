from django.urls import path

urlpatterns = [
    path('/'),  # get all investments / post - create investment (broker only)
    path('/:id'),  # get specific investment
]

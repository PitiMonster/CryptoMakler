from django.urls import path

urlpatterns = [
    path('', lambda:''),  # get all invitations / post - create invitation (sender only)
    path(':id', lambda:''),  # post - accept invitation (receiver only) / del - remove invitation
]

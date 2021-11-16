from django.urls import path

urlpatterns = [
    path(''),  # get all invitations / post - create invitation (sender only)
    path(':id'),  # post - accept invitation (receiver only) / del - remove invitation
]

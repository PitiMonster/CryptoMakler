from django.urls import path
from ..views import FundsListView, FundInvitationView

urlpatterns = [
    path('', FundsListView.as_view()),  # get all funds / post - create fund
    path(':id', lambda:''),  # get specific fund / del - remove fund
    # del - remove investment / patch - edit investment data
    path(':id/investment/:investmentId', lambda:''),
    path('<int:fund_id>/invitations/', FundInvitationView.as_view())
]

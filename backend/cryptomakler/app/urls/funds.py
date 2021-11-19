from django.urls import path
from ..views import FundsListView, FundInvitationView,  FundView, FundInvestmentView

urlpatterns = [
    path('', FundsListView.as_view()),  # get all funds / post - create fund
    # get specific fund / del - remove fund
    path('<int:fund_id>/', FundView.as_view()),
    # del - remove investment / patch - edit investment data
    path('<int:fund_id>/investment/<int:investment_id>/',
         FundInvestmentView.as_view()),
    path('<int:fund_id>/invitations/', FundInvitationView.as_view())
]

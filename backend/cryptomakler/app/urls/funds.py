from django.urls import path

from app.views.views import FundsListView, FundInvitationView, FundInvestmentView, FundView, FundAssetsView
# from ..views/funds import FundsListView, FundInvitationView,  FundView, FundInvestmentView


urlpatterns = [
    path('', FundsListView.as_view()),  # get all funds / post - create fund
    # get specific fund / del - remove fund
    path('<int:fund_id>/', FundView.as_view()),
    # del - remove investment / patch - edit investment data
    path('<int:fund_id>/investment/<int:investment_id>/',
         FundInvestmentView.as_view()),
    path('<int:fund_id>/invitations/', FundInvitationView.as_view()),
    # get all assets of fund / put - modify fund percents of existsing assets and add new ones
    path('<int:fund_id>/assets/', FundAssetsView.as_view()),
]

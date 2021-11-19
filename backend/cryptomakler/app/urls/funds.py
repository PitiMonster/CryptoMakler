from django.urls import path
from ..views import FundView, FundInvestmentView

urlpatterns = [
    path('', lambda:''),  # get all funds / post - create fund
    path('<int:fund_id>/', FundView.as_view()),  # get specific fund / del - remove fund
    path('<int:fund_id>/investment/<int:investment_id>/', FundInvestmentView.as_view()), # del - remove investment / patch - edit investment data

]

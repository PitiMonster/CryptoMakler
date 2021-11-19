from django.urls import path
from ..views import InvestmentsView

urlpatterns = [
    # get all investments
    path('', InvestmentsView.as_view()),
]

from django.urls import path
from app.views.views import InvestmentsView

urlpatterns = [
    # get all investments
    path('', InvestmentsView.as_view()),
]

from django.urls import path

from app.views.views import CoinsListView

urlpatterns = [
    path('', CoinsListView.as_view()),  # get all coins
]

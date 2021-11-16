from django.urls import path
from django.contrib.auth.views import PasswordResetView, PasswordChangeDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    RegisterView, TestTokenView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/validate/', TestTokenView.as_view(), name='token_validate'),

    path('reset/', PasswordResetView.as_view(), name='reset_password'),
    path('reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordChangeDoneView.as_view(), name='password_reset_done'),
    path('reset/complete/$', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
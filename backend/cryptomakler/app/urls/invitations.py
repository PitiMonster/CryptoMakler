from django.urls import path
from ..views import InvitationsListView, OneInvitationView
urlpatterns = [
    # get all invitations / post - create invitation (broker only)
    path('', InvitationsListView.as_view()),
    # post - accept invitation (investor only) / del - remove invitation
    path('<int:invitation_id>/', OneInvitationView.as_view()),
]

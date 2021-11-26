from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import models

from django.contrib.auth.models import User
from ..models import Fund, Invitation, Investment
from ..serializers import FundSerializer, InvestmentSerializer, InvitationSerializer


class InvitationsListView(APIView):
    def get(self, request):
        user_id = request.user.id

        try:
            invitations = Invitation.objects.filter(
                models.Q(sender=user_id) | models.Q(receiver=user_id))
            context = InvitationSerializer(invitations, many=True).data
        except Exception as e:
            return Response(str(e), status=status.HTTP_404_NOT_FOUND)

        return Response(context)


class FundInvitationView(APIView):
    def post(self, request, fund_id):
        try:
            user = User.objects.get(id=request.user.id)
            receiver = User.objects.get(username=request.POST.get('username', ''))
            fund = Fund.objects.get(id=fund_id)
            if request.user != fund.broker:
                return Response('You are not permitted to send invitation to this fund!', status=status.HTTP_403_FORBIDDEN)

            if Invitation.objects.filter(sender=user, receiver=receiver, fund=fund).exists():
                raise Exception('Invitation already sent!')

            if Investment.objects.filter(fund=fund, investor=receiver).exists():
                raise Exception('User already belongs to this fund!')

            data = {
                "sender": user,
                "receiver": receiver,
                "fund": fund,
            }

            invitation = InvitationSerializer().create(data)
            invitation.save()
            return Response(FundSerializer(fund).data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


class OneInvitationView(APIView):
    def post(self, request, invitation_id):
        invitation = Invitation.objects.get(id=invitation_id)
        if request.user != invitation.receiver:
            return Response('You are not permitted to response to this invitation!', status=status.HTTP_403_FORBIDDEN)

        investment = InvestmentSerializer().create(
            {"fund": invitation.fund, "investor": invitation.receiver})
        investment.save()

        invitation.delete()

        return Response('', status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, invitation_id):
        try:
            invitation = Invitation.objects.get(id=invitation_id)

            if request.user != invitation.receiver:
                return Response('You are not permitted to response to this invitation!', status=status.HTTP_403_FORBIDDEN)

            invitation.delete()
        except Exception as e:
            return Response("Invitation with provided id does not exist", status=status.HTTP_400_BAD_REQUEST)

        return Response('', status=status.HTTP_204_NO_CONTENT)

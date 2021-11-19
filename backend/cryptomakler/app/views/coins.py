from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User
from ..models import Coin
from ..serializers import CoinSerializer


class CoinsListView(APIView):

    def get(self, request):
        user_id = request.user.id

        user = User.objects.get(id=user_id)
        if user.userprofile.role != 'BRK':
            return Response('You are not permitted to this action!', status=status.HTTP_403_FORBIDDEN)

        try:
            coins = Coin.objects.all()
            context = CoinSerializer(coins, many=True).data
        except Exception as e:
            return Response("Error while preparing coins list!", status=status.HTTP_404_NOT_FOUND)

        return Response(context)

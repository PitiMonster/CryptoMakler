from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models import Coin, Asset, Fund
from ..serializers import AssetSerializer


from app.apps import APIClient

import json


class FundAssetsView(APIView):
    def get(self, request, fund_id):
        user_id = request.user.id
        fund = Fund.objects.get(id=fund_id)

        if(user_id != fund.broker.id):
            return Response('You are not permitted to this action!', status=status.HTTP_403_FORBIDDEN)
        try:
            assets = Asset.objects.filter(fund=fund)
            context = AssetSerializer(assets, many=True).data
            for asset in context:

                coin_price = APIClient.getCoinPrice(asset.coin)
                asset["total_value"] = asset['coin_amount'] * coin_price
        except Exception as e:
            print(e)
            return Response('Error while getting assets!', status=status.HTTP_400_BAD_REQUEST)

        return Response(context)

    def put(self, request, fund_id):
        try:
            user_id = request.user.id
            fund = Fund.objects.get(id=fund_id)

            if(user_id != fund.broker.id):
                return Response('You are not permitted to this action!', status=status.HTTP_403_FORBIDDEN)

            body = json.loads(request.body)
            coins = body['coins']
            sum_of_percents = 0
            for coin in coins:
                sum_of_percents += float(coin['percent'])

            if (sum_of_percents != 100):
                return Response('Bad division of assets! Sum of percents must equal 100', status=status.HTTP_400_BAD_REQUEST)

            assets = Asset.objects.filter(fund=fund_id)

            for asset in assets.iterator():
                print('siema 1')
                asset.fund_percent = 0
                asset.save()

            for coin in coins:
                coinObject = Coin.objects.get(id=coin['id'])
                (asset, _) = Asset.objects.get_or_create(
                    coin=coinObject, fund=fund)
                print(asset)
                asset.fund_percent = coin['percent']
                asset.save()

            assets = Asset.objects.filter(fund=fund_id)
            context = AssetSerializer(assets, many=True).data

            return Response(context)

        except Exception as e:
            return Response(f'Updating assets error: {str(e)}', status=status.HTTP_400_BAD_REQUEST)

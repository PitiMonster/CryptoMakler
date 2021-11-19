from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import models

from django.contrib.auth.models import User
from ..models import Fund, Investment
from ..serializers import FundSerializer

from ..enums import InvestmentOperationEnum
from ..utils import is_float

from app.apps import APIClient


class FundsListView(APIView):

    def get(self, request):
        user_id = request.user.id

        user = User.objects.get(id=user_id)
        if (user.userprofile.role != 'BRK'):
            return Response('You are not permitted to this action!', status=status.HTTP_403_FORBIDDEN)

        try:
            funds = Fund.objects.filter(broker=user_id)
            context = FundSerializer(funds, many=True).data
        except Exception as e:
            return Response("Funds for that broker does not exist!", status=status.HTTP_404_NOT_FOUND)

        return Response(context)

    def post(self, request):
        user = User.objects.get(id=request.user.id)

        data = {
            "name": request.POST.get('name', ''),
            "broker": user,
            "total_value": 0,
            "fee": request.POST.get('fee', 0)
        }

        try:
            fundSerializer = FundSerializer(data={**data, "broker": user.id})
            fundSerializer.is_valid(raise_exception=True)
            fund = fundSerializer.create(data)
            fund.save()
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        return Response(FundSerializer(fund).data, status=status.HTTP_201_CREATED)


class FundView(APIView):
    def get(self, request, fund_id):
        try:
            fund = Fund.objects.get(id=fund_id, broker=request.user)

            context = FundSerializer(fund).data

            return Response(context, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({str(e)}, status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request, fund_id):
        try:
            fund = Fund.objects.get(id=fund_id, broker=request.user)
            fund.delete()
            return Response(f'Fund deleted successfully', status.HTTP_200_OK)
        except models.ObjectDoesNotExist:
            return Response("Cannot delete fund with specified id", status=status.HTTP_404_NOT_FOUND)


class FundInvestmentView(APIView):
    def patch(self, request, fund_id, investment_id):
        try:
            investment = Investment.objects.get(id=investment_id, fund=fund_id)
            if investment.fund.broker != request.user:
                raise Exception('You are not authorized!')

            fiat_amount = request.POST.get('amount', None)
            transaction_type = request.POST.get('type', None)

            if transaction_type is None:
                raise Exception('Field `type` must be specified!')

            if transaction_type != InvestmentOperationEnum.WITHDRAW_ALL:
                if fiat_amount is None:
                    raise Exception('Field `amount` must be specified!')
                if not is_float or float(fiat_amount) <= 0:
                    raise Exception('Field `amount` must be greater than 0!')

            fiat_amount = float(fiat_amount)
            # TODO calculate share_price
            share_price = 1.0

            share_diff_amount = fiat_amount / share_price
            if transaction_type == InvestmentOperationEnum.WITHDRAW_ALL:
                investment.share_amount = 0.0
                investment.initial_value = 0.0

            elif transaction_type == InvestmentOperationEnum.WITHDRAW:
                if share_diff_amount > investment.share_amount:
                    raise Exception('Investor does not have enough funds')

                investment.initial_value -= investment.initial_value * \
                    share_diff_amount / investment.share_amount
                investment.share_amount -= share_diff_amount

            elif transaction_type == InvestmentOperationEnum.DEPOSIT:
                investment.share_amount += share_diff_amount
                investment.initial_value += fiat_amount

            else:
                raise Exception('Incorrect value in field `type`')

            investment.save()

            return Response(f'Investment updated successfully', status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({str(e)}, status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request, fund_id, investment_id):
        try:
            investment = Investment.objects.get(id=investment_id, fund=fund_id)
            if investment.fund.broker != request.user:
                raise Exception('You are not authorized!')

            investment.delete()
            return Response(f'Fund deleted successfully', status.HTTP_204_NO_CONTENT)
        except models.ObjectDoesNotExist:
            return Response("Cannot delete fund with specified id", status=status.HTTP_404_NOT_FOUND)

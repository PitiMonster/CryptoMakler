from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models import Investment
from ..serializers import InvestmentSerializer


class InvestmentsView(APIView):

    def get(self, request):
        user_id = request.user.id

        try:
            investments = Investment.objects.filter(investor=user_id)
            context = InvestmentSerializer(investments, many=True).data
        except Exception as e:
            return Response(str(e), status=status.HTTP_404_NOT_FOUND)

        return Response(context)

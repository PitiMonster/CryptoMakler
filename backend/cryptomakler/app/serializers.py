from rest_framework import serializers

from .models import User, Fund, Investment, Coin, Asset, Invitation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'role', 'email']


class FundSerializer(serializers.ModelSerializer):
    investors = serializers.SerializerMethodField()

    def get_investors(self, obj):
        investments = InvestmentSummarySerializer(obj.investments, many=True).data
        return investments


    class Meta:
        model = Fund
        fields = '__all__'
        validators = []

    def validate(self, data):
        """
        Check if fee is positive and less than 100
        """
        print(data)
        if float(data["fee"]) > 100 or float(data["fee"]) < 0:
            raise serializers.ValidationError(
                "Fee must be positive and less than 100")
        return data


class InvestmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investment
        fields = '__all__'


class InvestmentSummarySerializer(serializers.ModelSerializer):
    investor = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Investment
        fields = ['investor', 'share_amount']


class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coin
        fields = '__all__'


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'


class InvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitation
        fields = '__all__'

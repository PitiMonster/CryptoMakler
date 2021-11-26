from rest_framework import serializers

from .models import User, Fund, Investment, Coin, Asset, Invitation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'role', 'email']


class FundSerializer(serializers.ModelSerializer):
    investors = serializers.SerializerMethodField()
    total_value = serializers.FloatField(source='calculate_total_price')

    def get_investors(self, obj):
        investments = InvestmentSummarySerializer(
            obj.investments, many=True).data
        return investments

    class Meta:
        model = Fund
        fields = '__all__'
        validators = []

    def validate(self, data):
        """
        Check if fee is positive and less than 100
        """
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

    investor_id = serializers.SerializerMethodField()
    def get_investor_id(self, obj):
        return obj.investor.id

    class Meta:
        model = Investment
        fields = ['investor', 'investor_id', 'share_amount']


class InvestmentListSerializer(serializers.ModelSerializer):
    fund = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )

    total_value = serializers.FloatField(source='calculate_total_price')

    class Meta:
        model = Investment
        fields = ['fund', 'total_value']


class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coin
        fields = ["id", 'name']


class AssetSerializer(serializers.ModelSerializer):
    total_value = serializers.FloatField(source='calculate_total_price')
    coin = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )

    coin_id = serializers.SerializerMethodField()
    def get_coin_id(self, obj):
        return obj.coin.id

    class Meta:
        model = Asset
        fields = '__all__'


class InvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitation
        fields = '__all__'

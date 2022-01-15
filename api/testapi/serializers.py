from rest_framework import serializers
from .models import Stock, StockOrder, User, UserPortfolio


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('id', 'name', 'price')


class StockOrderSerializer(serializers.ModelSerializer):
    total_price = serializers.FloatField(read_only=True)

    class Meta:
        model = StockOrder
        fields = ('id', 'stock', 'quantity', 'total_price')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['stock'] = StockSerializer(instance.stock).data
        # response['user'] = UserSerializer(instance.user).data
        return response


class UserPortfolioSerializer(serializers.ModelSerializer):
    total_amount = serializers.FloatField(read_only=True)
    stock_order = StockOrderSerializer(many=True)

    # def get_stock_order(self, obj):
    #     stock_order = StockOrder.objects.filter(stock__orders = obj)
    #     serializer = StockOrderSerializer(stock_order, many=True)
    #     return serializer.daat

    class Meta:
        model = UserPortfolio
        fields = ('id', 'user', 'stock_order', 'total_amount')

    def create(self, validated_data):
        stock_order_data = validated_data.pop('stock_order')
        user_profolio = UserPortfolio.objects.create(**validated_data)
        for stock_order_data in stock_order_data:
            StockOrder.objects.create(user_profolio = user_profolio, **stock_order_data)
        return user_profolio

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['stock_order'] = StockSerializer(instance.stock_order).data
        response['user'] = UserSerializer(instance.user).data
        return response


    # def create(self, validated_data):
    #     return StockOrder(**validated_data)

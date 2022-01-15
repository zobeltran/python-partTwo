from django.shortcuts import render
from rest_framework import viewsets
from .models import Stock, UserPortfolio, StockOrder
from .serializers import StockOrderSerializer, StockSerializer, UserPortfolioSerializer

# Create your views here.
class StockView(viewsets.ModelViewSet):

    def get_serializer_class(self):
        return StockSerializer

    def get_queryset(self):
        return Stock.objects.all()
    
    
class UserPortfolioView(viewsets.ModelViewSet):

    def get_serializer_class(self):
        return UserPortfolioSerializer

    def get_queryset(self):
        return UserPortfolio.objects.all()

class StockOrderView(viewsets.ModelViewSet):

    def get_serializer_class(self):
        return StockOrderSerializer

    def get_queryset(self):
        return StockOrder.objects.all()
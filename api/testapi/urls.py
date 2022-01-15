import imp
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('stocks', views.StockView, 'stock')
router.register('UserPortfolio', views.UserPortfolioView, 'UserPortfolio')
router.register('stockOrder', views.StockOrderView, 'stockOrder')

urlpatterns = [
    path('', include(router.urls)) 
]
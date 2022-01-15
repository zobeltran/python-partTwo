from django.contrib import admin
from .models import Stock, StockOrder, UserPortfolio

# Register your models here.
admin.site.register(Stock)
admin.site.register(StockOrder)
admin.site.register(UserPortfolio)

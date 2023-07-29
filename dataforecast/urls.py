from django.urls import path

from .views import ForecastCategorySale, ForecastItemSale, create_forecast, forecast_prophet, forecast_autoarima
from .forecast import get_period

urlpatterns = [
    path('forecast-category-sales', ForecastCategorySale.as_view(),
         name='forecast_category_sales'),
    path('forecast-item-sales', ForecastItemSale.as_view(),
         name='forecast_item_sales'),
    path('create-forecast', create_forecast, name='create_forecast'),
    path('forecast-prophet', forecast_prophet, name='forecast_prophet'),
    path('forecast-autoarima', forecast_autoarima, name='forecast_autoarima'),
    path('periods', get_period, name='create_forecast')
]

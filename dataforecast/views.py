from django.shortcuts import render
from django.views.generic import ListView

from .models import *
from .forecast import predict_autoarima, predict_prophet, item_forecast


class ForecastCategorySale(ListView):
    model = ForecastCategorySales
    template_name = 'dataforecast/forecast_category_sales.html'
    context_object_name = 'forecast'
    paginate_by = 100

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet count of sale goods
        context['items_by_category_count'] = ForecastCategorySales.objects.all().count
        return context


class ForecastItemSale(ListView):
    model = ForecastItemSales
    template_name = 'dataforecast/forecast_item_sales.html'
    context_object_name = 'forecast'
    paginate_by = 441

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet count of sale goods
        context['items_sales_forecast_count'] = ForecastItemSales.objects.all().count
        return context


def create_forecast(request):
    return render(request, 'dataforecast/create_forecast.html')


def forecast_prophet(request):
    predict_prophet()
    item_forecast()
    success_p = 'Прогноз по модели Prophet выполнен успешно!'
    return render(request, 'dataforecast/create_forecast.html', context={'success_p': success_p})


def forecast_autoarima(request):
    predict_autoarima()
    item_forecast()
    success_a = 'Прогноз по модели AutoArima выполнен успешно!'

    return render(request, 'dataforecast/create_forecast.html', context={'success_a': success_a})

from django.shortcuts import render
from prophet import Prophet
from pmdarima import auto_arima
import pandas as pd
import datetime
from datetime import timedelta
import math

from datasales.models import SalesByCategory, Sales
from dataset.models import CategoryGoods, Goods
from dataforecast.models import ForecastCategorySales, ForecastItemSales
from .forms import ForecastForm


# Период фактических данных в днях, как базы для прогноза продаж
base_days = 70  # default
# Период в днях для прогноза продаж
forecast_days = 28  # default


def get_period(request):
    global base_days
    global forecast_days
    form = ForecastForm()
    if request.method == 'POST':
        form = ForecastForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            p1 = form.cleaned_data.get("base_period")
            p2 = form.cleaned_data.get("forecast_period")
            print(p1)
            print(p2)
            base_days = int(p1)
            forecast_days = int(p2)
    else:
        form = ForecastForm()
    return render(request,  'dataforecast/create_forecast.html', context={'form': form})


'''Расчет прогноза по категориям товаров с использованием модели Prophet'''


def predict_prophet():
    start_time = datetime.datetime.now()
    print(start_time)
    forecast_sales = pd.DataFrame(columns=['ds', 'code', 'forecast'])
    # Загрузка данных из базы продаж по категориям
    data_db = pd.DataFrame(
        list(SalesByCategory.objects.all().values('code', 'date', 'revenue')))
    data_db.index = pd.to_datetime(data_db.index)

    # Копия данных
    data = data_db.copy()
    # формат даты
    data['date'] = pd.to_datetime(data['date'])
    # Период в днях - база для рассчета прогноза
    first_date = data['date'][0]-timedelta(days=base_days)
    data = data[data['date'] >= first_date]
    data.set_index('date')

    # Лист с уникальными объектами - category
    item_list = data['code'].unique()

    # Расчет прогноза продаж по каждой категории
    print(f'Total items = {len(item_list)}')
    i = 0
    while i < len(item_list):
        print('!!Round-prophet = ', i)
        item_code = item_list[i]
        df_train = data[data['code'] == item_code]
        # строки с отстутствующими данными заполнить медианой
        df_train.fillna(df_train['revenue'].median(), inplace=True)

        # Rename the columns to 'ds' and 'y'
        df_train = df_train.rename(columns={'date': 'ds', 'revenue': 'y'})
        df_train.index = pd.to_datetime(df_train.index)
        df_train.drop(['code'], axis=1)

        # Creating and training the model: Initialize a prophet model and fit it to the data
        # creating the prophet model object
        model = Prophet()
        # fitting the data
        model.fit(df_train)

        # Generate future dates for the next 28 days
        future_dates = model.make_future_dataframe(
            periods=forecast_days, freq='D')
        # Make predictions
        forecast = model.predict(future_dates)

        # создаем DataFrame для прогноза
        df_forecast = pd.DataFrame(forecast, columns=['ds', 'yhat'])
        # отрицательные значения прогноза заменить на 0
        df_forecast.loc[df_forecast['yhat'] < 0, 'yhat'] = 0

        # 28 крайних периодов данных для train
        train_date = df_train['ds'][0]-timedelta(days=forecast_days)
        y_train = df_train[df_train['ds'] >= train_date]['y']

        # 28 периодов прогноза
        forecast_date = df_forecast['ds'][0]-timedelta(days=28)
        y_pred = df_forecast[df_forecast['ds'] >= forecast_date]['yhat']
        y_pred = y_pred.iloc[-forecast_days:]

        median_error = ((y_train.median()) / int(y_pred.median())-1)*100

        predict = pd.DataFrame(future_dates.iloc[-forecast_days:])
        predict['code'] = item_code
        predict['forecast'] = y_pred
        predict['median_error'] = median_error

        frames = [forecast_sales, predict]

        forecast_sales = pd.concat(frames)

        i += 1
    print('Prophet Predict CategorySales--OK')

    # Saving forecast from DataFrame directly to database via df_records
    ForecastCategorySales.objects.all().delete()
    df_records = forecast_sales.to_dict('records')
    model_instances = [ForecastCategorySales(
        date=record['ds'],
        weekday=record['ds'].weekday(),
        code=record['code'],
        forecast=round(record['forecast']),
        median_error=record['median_error']
    ) for record in df_records]
    ForecastCategorySales.objects.bulk_create(model_instances)

    # Add name to ForecastCategorySales table
    forecast_category_sales = ForecastCategorySales.objects.all()
    for i in forecast_category_sales:
        name = CategoryGoods.objects.get(code=i.code).name
        i.name = name
        i.save()

    print('Prophet ForecastCategorySales--OK')
    print(f'Период фактических данных в днях - {base_days}')
    print(f'Период в днях для прогноза продаж - {forecast_days}')
    print(f'Time: {datetime.datetime.now()-start_time}')


'''Расчет прогноза по категориям товаров с использованием модели AutoARIMA'''


def predict_autoarima():
    start_time = datetime.datetime.now()
    print(start_time)
    # 1.Подготовка данных по продажам для прогнозной модели
    forecast_sales = pd.DataFrame(columns=['date', 'code', 'forecast'])
    # Загрузка данных из базы продаж по категориям
    data_db = pd.DataFrame(
        list(SalesByCategory.objects.all().values('code', 'date', 'revenue')))
    # Копия данных
    data = data_db.copy()
    data.reset_index(drop=True, inplace=True)

    # формат даты
    data['date'] = pd.to_datetime(data['date'])
    # Период в днях - база для рассчета прогноза
    first_date = data['date'][0]-timedelta(days=base_days)
    data = data[data['date'] >= first_date]

    # Лист с уникальными объектами - category
    item_list = data['code'].unique()
    # Расчет прогноза по каждой категории
    start_test = data['date'][0]+timedelta(days=1)
    end_test = start_test+timedelta(days=forecast_days-1)
    # print('start_test==', start_test, 'end_test==', end_test)
    test_calendar_days = pd.date_range(start=start_test, end=end_test)
    # print('test_calendar_days: ', test_calendar_days)
    test = pd.DataFrame(test_calendar_days, columns=['date'])
    test['revenue'] = 0
    # реиндексация DataFrame  category_sales
    test.reset_index(drop=True, inplace=True)

    # 2. Расчет прогноза продаж по каждой категории
    i = 0
    while i < len(item_list):
        print('!!Round-autoarima = ', i)
        item_code = item_list[i]
        df_train = data[data['code'] == item_code]
        # строки с отстутствующими данными заполнить медианой
        df_train.fillna(df_train['revenue'].median(), inplace=True)

        # SARIMA model
        model = auto_arima(y=df_train.revenue, m=7)
        predictions = pd.Series(model.predict(n_periods=len(test)))
        predictions.index = test.index
        # создаем DataFrame для прогноза
        df_forecast = pd.DataFrame(predictions, columns=['forecast'])
        # predictions[0] = predictions[0].astype('Int64')
        df_forecast['code'] = item_code
        df_forecast['date'] = test_calendar_days
        median_error = ((df_train['revenue'].median()) /
                        int(df_forecast['forecast'].median())-1)*100
        df_forecast['median_error'] = median_error
        # print(df_forecast)

        frames = [forecast_sales, df_forecast]

        forecast_sales = pd.concat(frames)

        i += 1

    # Saving forecast from DataFrame directly to database via df_records
    ForecastCategorySales.objects.all().delete()
    df_records = forecast_sales.to_dict('records')
    model_instances = [ForecastCategorySales(
        date=record['date'],
        weekday=record['date'].weekday(),
        code=record['code'],
        forecast=round(record['forecast']),
        median_error=record['median_error']
    ) for record in df_records]
    ForecastCategorySales.objects.bulk_create(model_instances)

    # Add name to ForecastCategorySales table
    forecast_category_sales = ForecastCategorySales.objects.all()
    for i in forecast_category_sales:
        name = CategoryGoods.objects.get(code=i.code).name
        i.name = name
        i.save()

    print('AutoArima ForecastCategorySales--OK')
    print(f'Период фактических данных в днях - {base_days}')
    print(f'Период в днях для прогноза продаж - {forecast_days}')
    print(f'Time: {datetime.datetime.now()-start_time}')


'''Расчет прогноза по отдельным товарам'''


def item_forecast():
    start_time = datetime.datetime.now()
    print(start_time)
    # Загрузка данных из таблицы продаж по категориям
    data_db = pd.DataFrame(
        list(SalesByCategory.objects.all().values('date', 'weekday', 'code', 'name', 'revenue')))
    # data_db.index = pd.to_datetime(data_db.index)
    category_sales = data_db.copy()
    # реиндексация DataFrame  category_sales
    category_sales.reset_index(drop=True, inplace=True)
    # список уникальных кодов категорий в таблице продаж по категориям
    category_list = category_sales['code'].unique()

    # Загрузка данных из таблицы продаж по товарам
    item_db = pd.DataFrame(
        list(Sales.objects.all().values('date', 'weekday', 'code', 'category_id', 'revenue')))
    # item_db.index = pd.to_datetime(item_db.index)
    item_sales = item_db.copy()

    # создаем пустой список для долей товаров в категориях
    items_share = []

    # по каждой категории определим структуру/долю продаж товаров
    for i in category_list:
        # сумма продаж по категории
        total_category = category_sales[category_sales['code']
                                        == i]['revenue'].sum()
        # категория как id
        category_id = CategoryGoods.objects.get(code=i).id
        # Товары в данной категории
        sales_item = item_sales[item_sales['category_id'] == category_id]

        # рассчет доли продаж товара в категории
        for j in sales_item.code.unique():
            # Сумма продаж по товару в категрии
            item_sum = sales_item[sales_item['code'] == j]['revenue'].sum()
            # доля продаж товара в категрии
            share_item_sales = item_sum/total_category
            # создание таблицы с долей продаж в категриях по всем товарам
            frames = [i, j, share_item_sales]
            items_share.append(frames)

    # создание pd.DataFrame с долей продаж в категриях по всем товарам
    share = pd.DataFrame(items_share, columns=[
        'category_code', 'item_code', 'item_share'])

    forecast_category_sales = pd.DataFrame(list(
        ForecastCategorySales.objects.all().values('date', 'name', 'code', 'forecast')))

    total_item_forecast = forecast_category_sales.copy()
    total_item_forecast.rename(
        columns={'code': 'category_code', 'name': 'category'}, inplace=True)

    df_merged = pd.merge(total_item_forecast, share)

    print(f'Time: {datetime.datetime.now()-start_time}')

    # Saving forecast from DataFrame directly to database via df_records
    print('Start ForecastItemSales TABLE ...')
    ForecastItemSales.objects.all().delete()

    df_records = df_merged.to_dict('records')

    model_instances = [ForecastItemSales(
        date=record['date'],
        weekday=record['date'].weekday(),
        category=record['category'],
        code=record['item_code'],
        name='',
        item_forecast=0,
        revenue_forecast=record['forecast']*record['item_share'],

    ) for record in df_records]
    ForecastItemSales.objects.bulk_create(model_instances)
    print('ForecastItemSales - OK\n Add name to ForecastItemSales table ...\n',
          f'Time: {datetime.datetime.now()-start_time}')
    # Add the name and quantity of goods in pieces to the ForecastItemSales table
    forecast_category_sales = ForecastItemSales.objects.all()
    for i in forecast_category_sales:
        name = Goods.objects.get(code=i.code).name
        i.name = name
        price = float(Goods.objects.get(code=i.code).price)
        i.item_forecast = round(i.revenue_forecast/price)
        if i.item_forecast < 1:
            i.item_forecast = 1
        i.save()
    print('ForecastItemSales - Added name ... Added item_forecast ... OK!')
    print(f'Time: {datetime.datetime.now()-start_time}')
    print('item_forecast() -- OK!')

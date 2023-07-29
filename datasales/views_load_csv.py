from django.shortcuts import render, redirect

import pandas as pd
import sqlite3
from django.core.files.storage import FileSystemStorage
from .models import Sales, SalesLoading
from dataset.models import Goods
from .forms import AddSalesForm
import datetime


from dataset.services import do_slug


'''4.Загрузка списка проданных Товаров из csv file with pandas'''


def sales_loading(request):
    SalesLoading.objects.all().delete()
    print('start def sale_loading(): from csv')
    start = datetime.datetime.now()
    try:
        if request.method == 'POST' and request.FILES['myfile']:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            excel_file = uploaded_file_url
            print('excel_file:', excel_file)
            empexceldata = pd.read_csv("." + excel_file, encoding='utf-8')
            print('type(empexceldata):', type(empexceldata))

            conn = sqlite3.connect(
                'db.sqlite3')

            empexceldata.to_sql('datasales_salesloading',
                                conn, if_exists='replace')

            print('Загружено! Время загрузки = ',
                  datetime.datetime.now()-start)
            return render(request, 'loading/sales_loading.html', {
                'uploaded_file_url': uploaded_file_url, 'myfile': myfile, 'start': start
            })
    except Exception as identifier:
        print('Exception as identifier=', identifier)
        return render(request, 'loading/sales_loading.html', {'item_except': identifier})

    return render(request, 'loading/sales_loading.html', {})


'''4-1.Сохранение импортированного из csv файла списка проданных Товаров в Базу Данных'''


def csv_sales(request):
    print('Выполняется Функция csv_sales - загрузка продаж в БД')
    start = datetime.datetime.now()
    print(start)
    req = SalesLoading.objects.all()
    print('REG==', req)
    print('Выполняется загрузка продаж в БД ...')
    for i in req:
        goods = Goods.objects.filter(code=i.code)
        for good in goods:
            g_unit = good.unit
            g_unit_cost = good.unit_cost
            g_price = good.price
        try:
            Sales.objects.create(
                code=i.code,
                unit=g_unit,
                unit_cost=g_unit_cost,
                price=g_price,
                sales=i.sales,
                revenue=g_price*i.sales,
                gross_profit=i.sales*(g_price-g_unit_cost),
                date=i.date,
                weekday=i.date.weekday(),
                name_id=Goods.objects.get(code=i.code).id,
                category_id=Goods.objects.get(code=i.code).category_id
            )

            print(i.name, '-OK')

        except Exception as e:
            print('Exception as identifier=', e)
            return render(request, 'loading/sales_loading.html', {'item_except': e})
    end = datetime.datetime.now()
    print(end)
    print('Загружено в БД! Время загрузки продаж в БД = ', end-start)

    success = 'Загрузка и сохранение Goods в БД выполнена успешно!'

    return render(request, 'loading/sales_loading.html', context={'item_success': success})


'''4-2. Добавление продажи товара в список проданных Товаров  через ФОРМУ.'''


def add_sales(request):
    form = AddSalesForm()
    if request.method == 'POST':
        form = AddSalesForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            sales = form.cleaned_data.get("sales")
            date = form.cleaned_data.get("date")

            item = Goods.objects.filter(name=name)
            print(name)
            print(sales)
            print(date)
            for i in item:
                code = i.code
                unit = i.unit
                unit_cost = i.unit_cost
                p = i.price
                cat = i.category

            Sales.objects.create(
                date=date,
                weekday=date.weekday(),
                name=name,
                category=cat,
                sales=sales,
                code=code,
                unit=unit,
                unit_cost=unit_cost,
                price=p,
                revenue=p*sales,
                gross_profit=(p - unit_cost)*sales
            )

            return redirect('sales')

    context = {
        'form': form,
    }
    return render(request, 'forms/addSales.html', context)

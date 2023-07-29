from django.shortcuts import render, redirect
from django.views.generic import ListView
import datetime

from django.db.models import Sum


from .models import Sales, SalesByCategory, SalesBySupplier
from dataset.models import CategoryGoods, Supplier

'''1. Продажи по товарам'''


class SalesListView(ListView):
    model = Sales
    template_name = 'datasales/sales_list.html'
    context_object_name = 'items'
    paginate_by = 100

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet count of sale goods
        context['sale_count'] = Sales.objects.all().count
        return context


'''2. Продажи по категориям товаров'''


class SalesByCategoryListView(ListView):
    model = SalesByCategory
    template_name = 'datasales/sales_by_category_list.html'
    context_object_name = 'items'
    paginate_by = 30

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet count of sale goods
        context['sales_by_category_count'] = SalesByCategory.objects.all().count
        return context


'''3. Продажи по поставщикам товаров'''


class SalesBySupplierListView(ListView):
    model = SalesBySupplier
    template_name = 'datasales/sales_by_supplier_list.html'
    context_object_name = 'items'
    paginate_by = 30

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet count of sale goods
        context['sales_by_category_count'] = SalesBySupplier.objects.all().count
        return context


def create_sales_categories(requests):
    return render(requests, "group_sales/group_sales_by.html")


'''4. Формирование продаж по категориям товаров'''


def sales_group_by_category(requests):
    start = datetime.datetime.now()
    SalesByCategory.objects.all().delete()
    dates = Sales.objects.values_list("date", flat=True).distinct()
    for day in dates:
        print(day)
        cats = CategoryGoods.objects.all()
        for cat in cats:
            crs = Sales.objects.filter(date=day).filter(
                category_id=cat.id).aggregate(Sum('revenue'))
            revenue = (crs['revenue__sum'])
            grp = Sales.objects.filter(date=day).filter(
                category_id=cat.id).aggregate(Sum('gross_profit'))
            gross_profit = (grp['gross_profit__sum'])
            SalesByCategory.objects.create(
                date=day, weekday=day.weekday(), code=cat.code, name=cat.name, revenue=revenue, gross_profit=gross_profit)
            print(day, day.weekday(), cat.code, cat.name,
                  'revenue=', revenue, 'gross=', gross_profit)
    print('Загружено! Время загрузки = ',
          datetime.datetime.now()-start)
    return redirect('sales_by_category')


'''5. Формирование продаж по поставщикам товаров'''


def sales_group_by_supplier(requests):
    start = datetime.datetime.now()
    SalesBySupplier.objects.all().delete()
    dates = Sales.objects.values_list("date", flat=True).distinct()
    for day in dates:
        print(day)
        suppliers = Supplier.objects.all()
        for cat in suppliers:
            crs = Sales.objects.filter(date=day).filter(
                category_id=cat.id).aggregate(Sum('revenue'))
            revenue = (crs['revenue__sum'])
            grp = Sales.objects.filter(date=day).filter(
                category_id=cat.id).aggregate(Sum('gross_profit'))
            gross_profit = (grp['gross_profit__sum'])
            SalesBySupplier.objects.create(
                date=day, weekday=day.weekday(), code=cat.code, name=cat.name, revenue=revenue, gross_profit=gross_profit)
            print(day, day.weekday(), cat.code, cat.name,
                  'revenue=', revenue, 'gross=', gross_profit)
    print('Загружено! Время загрузки = ',
          datetime.datetime.now()-start)
    return redirect('sales_by_supplier')

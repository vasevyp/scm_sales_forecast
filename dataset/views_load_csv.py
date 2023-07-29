from django.shortcuts import render, redirect

import pandas as pd
import sqlite3
from django.core.files.storage import FileSystemStorage
from .models import Supplier, SupplierLoading,  Buier, BuierLoading, CategoryGoods, CategoryGoodsLoading, Goods, GoodsLoading
from .forms import AddSupplierForm, AddBuierForm, AddCategoryGoodsForm, AddGoodsForm


from .services import do_slug

'''1.Загрузка списка Поставщиков из csv file with pandas'''


def supplier_loading(request):
    print('start download_supplier')
    try:
        if request.method == 'POST' and request.FILES['myfile']:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            excel_file = uploaded_file_url
            print('excel_file:', excel_file)
            empexceldata = pd.read_csv("."+excel_file, encoding='utf-8')
            print('type(empexceldata):', type(empexceldata))

            conn = sqlite3.connect('db.sqlite3')
            empexceldata.to_sql('dataset_supplierloading',
                                conn, if_exists='replace')

            return render(request, 'loading/supplier_loading.html', {
                'uploaded_file_url': uploaded_file_url, 'myfile': myfile
            })
    except Exception as identifier:
        print('Exception as identifier=', identifier)
        return render(request, 'loading/supplier_loading.html', {'item_except': identifier})

    return render(request, 'loading/supplier_loading.html', {})


'''1-1.Сохранение импортированного из csv файла списка Поставщиков в Базу Данных'''


def csv_supplier(request):
    print('Выполняется Функция csv_supplier')
    supplier = SupplierLoading.objects.all()
    for s in supplier:
        try:
            Supplier.objects.create(
                name=s.name, code=s.code, address=s.address, contact=s.contact, slug=do_slug(s.name))
            print(s.name, ' -OK')
            s.delete()
        except Exception as e:
            print('Exception as identifier=', e)
            return render(request, 'loading/supplier_loading.html', {'loading_except': f'код {s.code} уже есть в базе поставщиков. -- {e}'})

    SupplierLoading.objects.all().delete()
    success = 'Загрузка и сохранение Supplier выполнена успешно!'

    return render(request, 'loading/supplier_loading.html', context={'supplier_success': success})


'''1-2. Добавление поставщика в базу данных Supplier через ФОРМУ.'''


def add_supplier(request):
    form = AddSupplierForm()
    if request.method == 'POST':
        form = AddSupplierForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            form.save()
            item = Supplier.objects.get(name=name)
            item.slug = do_slug(name)
            item.save()
            return redirect('supplier')

    context = {
        'form': form
    }
    return render(request, 'forms/addSupplier.html', context)


'''2.Загрузка списка Заказчиков из csv file with pandas'''


def buier_loading(request):
    print('start download_buier')
    try:
        if request.method == 'POST' and request.FILES['myfile']:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            excel_file = uploaded_file_url
            print('excel_file:', excel_file)
            empexceldata = pd.read_csv("."+excel_file, encoding='utf-8')
            print('type(empexceldata):', type(empexceldata))

            conn = sqlite3.connect('db.sqlite3')
            empexceldata.to_sql('dataset_buierloading',
                                conn, if_exists='replace')

            return render(request, 'loading/buier_loading.html', {
                'uploaded_file_url': uploaded_file_url, 'myfile': myfile
            })
    except Exception as identifier:
        print('Exception as identifier=', identifier)
        return render(request, 'loading/buier_loading.html', {'item_except': identifier})

    return render(request, 'loading/buier_loading.html', {})


'''2-1.Сохранение импортированного из csv файла списка Заказчиков в Базу Данных'''


def csv_buier(request):
    print('Выполняется Функция post_impex_supplier')
    buier = BuierLoading.objects.all()
    for s in buier:
        try:
            Buier.objects.get_or_create(
                name=s.name, code=s.code, address=s.address, contact=s.contact, slug=do_slug(s.name))
            print(s.name, ' -OK')
            s.delete()
        except Exception as e:
            print('Exception as identifier=', e)
            return render(request, 'loading/buier_loading.html', {'loading_except': f'код {s.code} уже есть в базе заказчиков. -- {e}'})
    success = 'Загрузка и сохранение Buier выполнена успешно!'

    return render(request, 'loading/buier_loading.html', context={'buier_success': success})


'''2-2. Добавление закзчика в базу данных Buier через ФОРМУ.'''


def add_buier(request):
    form = AddBuierForm()
    if request.method == 'POST':
        form = AddBuierForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            form.save()
            item = Buier.objects.get(name=name)
            item.slug = do_slug(name)
            item.save()
            return redirect('buier')

    context = {
        'form': form
    }
    return render(request, 'forms/addBuier.html', context)


'''3.Загрузка списка Категорий товаров из csv file with pandas'''


def categorygoods_loading(request):
    print('start download_categoryitem')
    CategoryGoodsLoading.objects.all().delete()
    try:
        if request.method == 'POST' and request.FILES['myfile']:

            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            excel_file = uploaded_file_url
            print('excel_file:', excel_file)
            empexceldata = pd.read_csv("."+excel_file, encoding='utf-8')
            print('type(empexceldata):', type(empexceldata))

            conn = sqlite3.connect('db.sqlite3')
            empexceldata.to_sql('dataset_categorygoodsloading',
                                conn, if_exists='replace')

            return render(request, 'loading/category_goods_loading.html', {
                'uploaded_file_url': uploaded_file_url, 'myfile': myfile
            })
    except Exception as identifier:
        print('Exception as identifier=', identifier)
        return render(request, 'loading/category_goods_loading.html', {'item_except': identifier})

    return render(request, 'loading/category_goods_loading.html', {})


'''3-1.Сохранение импортированного из csv файла списка Категории Товаров в Базу Данных'''


def csv_category_goods(request):
    print('Выполняется Функция csv_category_goods')
    category = CategoryGoodsLoading.objects.all()
    for cat in category:
        try:
            print('Это объект = ', cat)
            CategoryGoods.objects.create(
                name=cat.name, code=cat.code, slug=do_slug(cat.name))
            print(cat.name, ' -OK.')
            cat.delete()
        except Exception as e:
            print('Exception as identifier=', e)
            return render(request, 'loading/category_item_loading.html', {'loading_except': f'код {cat.code} или имя {cat.name} уже есть в базе категорий товаров. -- {e}'})
    success = 'Загрузка и сохранение CategoryItem выполнена успешно!'
    return render(request, 'loading/category_goods_loading.html', context={'categoryitem_success': success})


'''3-2. Добавление  категории для товара/ингредиента в базу данных CategoryItem через ФОРМУ.'''


def add_category_goods(request):
    form = AddCategoryGoodsForm()
    if request.method == 'POST':
        form = AddCategoryGoodsForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            form.save()
            s = CategoryGoods.objects.get(name=name)
            s.slug = do_slug(name)
            s.save()
            return redirect('category')

    context = {
        'form': form
    }
    return render(request, 'forms/addGoodsCategory.html', context)


'''4.Загрузка списка Товаров из csv file with pandas'''


def goods_loading(request):
    GoodsLoading.objects.all().delete()
    print('start download_goods')
    try:
        if request.method == 'POST' and request.FILES['myfile']:

            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            excel_file = uploaded_file_url
            print('excel_file:', excel_file)
            empexceldata = pd.read_csv("."+excel_file, encoding='utf-8')
            print('type(empexceldata):', type(empexceldata))

            conn = sqlite3.connect('db.sqlite3')
            empexceldata.to_sql('dataset_goodsloading',
                                conn, if_exists='replace')

            return render(request, 'loading/goods_loading.html', {
                'uploaded_file_url': uploaded_file_url, 'myfile': myfile
            })
    except Exception as identifier:
        print('Exception as identifier=', identifier)
        return render(request, 'loading/goods_loading.html', {'item_except': identifier})

    return render(request, 'loading/goods_loading.html', {})


'''4-1.Сохранение импортированного из csv файла списка Товаров в Базу Данных'''


def csv_goods(request):
    print('Выполняется Функция csv_goods')
    req = GoodsLoading.objects.all()
    for i in req:
        s_id = Supplier.objects.get(name=i.supplier).id
        c_id = CategoryGoods.objects.get(name=i.category).id
        try:
            Goods.objects.create(
                name=i.name,
                code=i.code,
                unit=i.unit,
                unit_cost=i.unit_cost,
                price=i.unit_price,
                description=i.description,
                category_id=c_id,
                supplier_id=s_id,
                delivery_time=i.delivery_time,
                supply_pack=i.supply_pack,
                pack_weight=i.pack_weight,
                pack_length=i.pack_length,
                pack_width=i.pack_width,
                pack_height=i.pack_height,
                slug=do_slug(i.name)
            )

            print(i.name, '-OK')

        except Exception as e:
            print('Exception as identifier=', e)
            return render(request, 'loading/goods_loading.html', {'loading_except': f'код {i.code} уже есть в базе товаров. -- {e}'})
    GoodsLoading.objects.all().delete()
    success = 'Загрузка и сохранение Goods выполнена успешно!'

    return render(request, 'loading/goods_loading.html', context={'item_success': success})


'''4-2. Добавление товара/ингредиента в список Товаров  через ФОРМУ.'''


def add_goods(request):
    form = AddGoodsForm()
    if request.method == 'POST':
        form = AddGoodsForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            form.save()
            it = Goods.objects.get(name=name)
            it.slug = do_slug(name)
            it.save()
            return redirect('goods')
    context = {
        'form': form
    }
    return render(request, 'forms/addGoods.html', context)

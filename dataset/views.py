from django.shortcuts import render
from django.views.generic import ListView

from .models import *


class CategoryListView(ListView):
    model = CategoryGoods
    template_name = 'dataset/category_list.html'
    context_object_name = 'categories'
    paginate_by = 12


def supplier_list(request):
    supplier = Supplier.objects.all()
    context = {
        'suppliers': supplier
    }

    return render(request, 'dataset/supplier_list.html', context)


class BuierListView(ListView):
    model = Buier
    template_name = 'dataset/buier_list.html'
    context_object_name = 'buiers'


class GoodsListView(ListView):
    model = Goods
    template_name = 'dataset/goods_list.html'
    context_object_name = 'items'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet count of goods
        context['goods_count'] = Goods.objects.all().count
        return context


def dataset_loading(requests):

    return render(requests, 'loading/dataset_loading.html')

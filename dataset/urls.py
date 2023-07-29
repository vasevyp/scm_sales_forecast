
from django.urls import path

from .views import CategoryListView, supplier_list, BuierListView, GoodsListView, dataset_loading
from .views_load_csv import supplier_loading, csv_supplier, buier_loading, csv_buier, categorygoods_loading, csv_category_goods,  goods_loading, csv_goods, add_supplier, add_buier, add_category_goods, add_goods

urlpatterns = [
    path('category', CategoryListView.as_view(), name='category'),
    path('supplier', supplier_list, name='supplier'),
    path('buier', BuierListView.as_view(), name='buier'),
    path('goods', GoodsListView.as_view(), name='goods'),
    path('loading', dataset_loading, name='dataset_loading'),
    path('supplier-loading/', supplier_loading, name='supplier_loading'),  # +
    path('csv-supplier/', csv_supplier, name='csv_supplier'),  # +
    path('buier-loading/', buier_loading, name='buier_loading'),  # +
    path('csv-buier/', csv_buier, name='csv_buier'),  # +
    path('categorygoods-loading', categorygoods_loading,
         name='categorygoods_loading'),  # +
    path('csv-categorygoods/', csv_category_goods,
         name='csv_categorygoods'),  # +
    path('goods-loading', goods_loading, name='goods_loading'),
    path('csv-goods/', csv_goods, name='csv_goods'),
    path('add-supplier/', add_supplier, name='add_supplier'),
    path('add-buier/', add_buier, name='add_buier'),
    path('add-categorygoods/', add_category_goods, name='add_categorygoods'),
    path('add-goods/', add_goods, name='add_goods'),

]

from django.urls import path
from . views import SalesListView, SalesByCategoryListView, SalesBySupplierListView, create_sales_categories, sales_group_by_category, sales_group_by_supplier
from . views_load_csv import sales_loading, csv_sales,  add_sales


urlpatterns = [
    path('sales', SalesListView.as_view(), name='sales'),
    path('sales-by-category', SalesByCategoryListView.as_view(),
         name='sales_by_category'),
    path('sales-by-supplier', SalesBySupplierListView.as_view(),
         name='sales_by_supplier'),
    path('sales-loading/', sales_loading, name='sales_loading'),
    path('csv-sales/', csv_sales, name='csv_sales'),
    path('add-sales/', add_sales, name='add_sales'),
    path('create-sales-categories', create_sales_categories,
         name='create_sales_categories'),
    path('sales_group_by_category', sales_group_by_category,
         name='sales_group_by_category'),
    path('sales_group_by_supplier', sales_group_by_supplier,
         name='sales_group_by_supplier'),

]

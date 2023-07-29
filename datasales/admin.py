from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Sales, SalesLoading, SalesByCategory, SalesBySupplier


@admin.register(Sales)
class SalesAdmin(ImportExportModelAdmin):
    list_display = ['date', 'code', 'name', 'category', 'unit', 'unit_cost',
                    'price', 'sales', 'revenue', 'weekday', 'gross_profit']
    # prepopulated_fields = {'name': ('name',)}
    save_on_top = True
    search_fields = ('code',)
    list_filter = ('name',)


@admin.register(SalesLoading)
class SalesLoadingAdmin(ImportExportModelAdmin):
    list_display = ['date', 'code', 'name', 'sales']
    save_on_top = True
    search_fields = ('name',  'code')
    list_filter = ('name', )


@admin.register(SalesByCategory)
class SalesByCategoryAdmin(ImportExportModelAdmin):
    list_display = ['date', 'weekday', 'code',
                    'name', 'revenue', 'gross_profit']
    save_on_top = True
    search_fields = ('name', )
    list_filter = ('name',)


@admin.register(SalesBySupplier)
class SalesBySupplierAdmin(ImportExportModelAdmin):
    list_display = ['date', 'weekday', 'code',
                    'name', 'revenue', 'gross_profit']
    save_on_top = True
    search_fields = ('name', )
    list_filter = ('name',)

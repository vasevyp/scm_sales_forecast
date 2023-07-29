from django.contrib import admin


from import_export.admin import ImportExportModelAdmin

from .models import CategoryGoods, Supplier, Goods, Buier, SupplierLoading, BuierLoading, CategoryGoodsLoading, GoodsLoading


@admin.register(Supplier)
class SupplierAdmin(ImportExportModelAdmin):
    list_display = ['code', 'name', 'contact',
                    'address', 'slug', 'created_date']
    prepopulated_fields = {'slug': ('name',)}
    save_on_top = True
    search_fields = ['name',]
    list_filter = ('name', 'code')


@admin.register(SupplierLoading)
class SupplierLoadingAdmin(ImportExportModelAdmin):
    list_display = ['code', 'name', 'contact', 'address']
    save_on_top = True
    search_fields = ['name',]
    list_filter = ('name', 'code')


@admin.register(Buier)
class BuierAdmin(ImportExportModelAdmin):
    list_display = ['code', 'name', 'contact',
                    'address', 'slug', 'created_date']
    prepopulated_fields = {'slug': ('name',)}
    save_on_top = True
    search_fields = ['name',]
    list_filter = ('name', 'code')


@admin.register(BuierLoading)
class BuierLoadingAdmin(ImportExportModelAdmin):
    list_display = ['code', 'name', 'contact', 'address']
    save_on_top = True
    search_fields = ['name',]
    list_filter = ('name', 'code')


@admin.register(CategoryGoods)
class CategoryItemAdmin(ImportExportModelAdmin):
    list_display = ['code', 'name', 'slug', 'created_date']
    prepopulated_fields = {'slug': ('name',)}
    save_on_top = True
    search_fields = ['name',]
    list_filter = ('name',)


@admin.register(CategoryGoodsLoading)
class CategoryItemLoadingAdmin(ImportExportModelAdmin):
    list_display = ['code', 'name', ]
    save_on_top = True
    search_fields = ['name', 'code']
    list_filter = ('name',)


@admin.register(Goods)
class ItemAdmin(ImportExportModelAdmin):
    list_display = ['code', 'name', 'category', 'supplier', 'unit_cost', 'price', 'delivery_time',
                    'supply_pack', 'pack_weight', 'pack_length', 'pack_width', 'pack_height', 'created_date']
    prepopulated_fields = {'slug': ('name',)}
    save_on_top = True
    search_fields = ('name',  'code')
    list_filter = ('name', 'code')


@admin.register(GoodsLoading)
class ItemLoadingAdmin(ImportExportModelAdmin):
    list_display = ['code', 'name', 'category', 'supplier', 'unit_cost', 'unit_price',
                    'delivery_time', 'supply_pack', 'pack_weight', 'pack_length', 'pack_width', 'pack_height']
    save_on_top = True
    search_fields = ('name',  'code')
    list_filter = ('name', 'code')

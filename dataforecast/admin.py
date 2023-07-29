from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import ForecastCategorySales


@admin.register(ForecastCategorySales)
class ForecastCategorySalesAdmin(ImportExportModelAdmin):
    list_display = ['date', 'weekday', 'code',
                    'name', 'forecast', 'median_error']
    save_on_top = True
    search_fields = ('name', )
    list_filter = ('name',)

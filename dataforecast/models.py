from django.db import models
from django.urls import reverse


class ForecastCategorySales(models.Model):
    date = models.DateField(verbose_name='Дата',
                            help_text="'2022-08-18", null=True)
    weekday = models.PositiveIntegerField(
        verbose_name='День недели', null=True)
    code = models.DecimalField(
        max_digits=6, help_text="6 цифр", decimal_places=0)
    name = models.CharField(
        max_length=200, help_text="Не более 200 знаков", db_index=True, verbose_name='Категория')
    forecast = models.DecimalField(
        max_digits=20, help_text="Не более 10 знаков", decimal_places=2, default=0, blank=True, null=True)
    median_error = models.DecimalField(
        max_digits=20, decimal_places=2, default=0, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('item', kwargs={'name': self.name})

    class Meta:
        ordering = ['name']
        verbose_name = 'Прогноз Продаж по Category'
        verbose_name_plural = 'Прогнозы Продаж по Category'

    def __str__(self):
        return self.name


class ForecastItemSales(models.Model):
    date = models.DateField(verbose_name='Дата',
                            help_text="'2022-08-18", null=True)
    weekday = models.PositiveIntegerField(
        verbose_name='День недели', null=True)
    category = models.CharField(
        max_length=200, help_text="Не более 200 знаков", blank=True, verbose_name='Категория')
    code = models.IntegerField()
    name = models.CharField(
        max_length=200, help_text="Не более 200 знаков", blank=True, verbose_name='Наименование')
    revenue_forecast = models.FloatField(blank=True, null=True)
    item_forecast = models.IntegerField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('item', kwargs={'name': self.name})

    class Meta:
        ordering = ['code', 'date']
        verbose_name = 'Прогноз Продаж по Товарам'
        verbose_name_plural = 'Прогнозы Продаж по Товарам'

    def __str__(self):
        return self.name

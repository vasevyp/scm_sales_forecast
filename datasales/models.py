from django.db import models
from django.urls import reverse

from dataset.models import Goods, CategoryGoods


UNITS = (
    (None, 'Выбрать ед.изм.'),
    ('кг', 'кг'),
    ('л', 'л'),
    ('шт.', ' шт.'),
)

'''1.Модель проданных продуктов'''


class Sales(models.Model):
    name = models.ForeignKey(
        Goods, related_name='name_sale', null=True, on_delete=models.PROTECT)
    code = models.DecimalField(max_digits=12, help_text="Не более 12 знаков",
                               decimal_places=0, null=True, verbose_name='Код')
    category = models.ForeignKey(
        CategoryGoods, related_name='category_sale', null=True, on_delete=models.PROTECT)
    unit = models.CharField(
        max_length=10, verbose_name='Ед.изм.',  choices=UNITS, null=True, default='шт.')
    unit_cost = models.PositiveIntegerField(
        verbose_name='cost, руб', default=1)
    price = models.PositiveIntegerField(verbose_name='Цена, руб', default=1)
    sales = models.PositiveIntegerField(verbose_name='Продано,шт.', default=1)
    revenue = models.DecimalField(
        max_digits=10, help_text="Не более 10 знаков", decimal_places=2, default=0, blank=True, null=True)
    gross_profit = models.DecimalField(
        max_digits=10, help_text="Не более 10 знаков", decimal_places=2, default=0, blank=True, null=True)
    date = models.DateField(verbose_name='Дата',
                            help_text="'2022-08-18", null=True)
    weekday = models.PositiveIntegerField(
        verbose_name='День недели', null=True)
    created_date = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('sale', kwargs={'name': self.name})

    class Meta:
        ordering = ['-date']
        verbose_name = 'Продажа'
        verbose_name_plural = 'Продажи'

    def __str__(self):
        return str(self.code)

    @property
    def get_revenue(self):
        return self.price*self.sold


'''2. Модель ЗАГРУЗКИ проданных товаров'''


class SalesLoading(models.Model):
    code = models.DecimalField(max_digits=12, help_text="Не более 12 знаков",
                               decimal_places=0, null=True, verbose_name='Код')
    name = models.CharField(
        max_length=200, help_text="Не более 200 знаков", db_index=True)
    sales = models.PositiveIntegerField(verbose_name='Продано,шт.', default=1)
    date = models.DateField(verbose_name='Дата',
                            help_text="'2022-08-18", null=True)

    def get_absolute_url(self):
        return reverse('item', kwargs={'name': self.name})

    class Meta:
        ordering = ['name']
        verbose_name = 'Продажа-Loading'
        verbose_name_plural = 'Продажи-Loading'

    def __str__(self):
        return self.name


'''3.Модель группировки проданных товаров по категориям'''


class SalesByCategory(models.Model):
    code = models.DecimalField(
        max_digits=6, help_text="6 цифр", decimal_places=0)
    name = models.CharField(
        max_length=200, help_text="Не более 200 знаков", db_index=True, verbose_name='Категория')
    date = models.DateField(verbose_name='Дата',
                            help_text="'2022-08-18", null=True)
    weekday = models.PositiveIntegerField(
        verbose_name='День недели', null=True)
    revenue = models.DecimalField(
        max_digits=10, help_text="Не более 10 знаков", decimal_places=2, default=0, blank=True, null=True)
    gross_profit = models.DecimalField(
        max_digits=10, help_text="Не более 10 знаков", decimal_places=2, default=0, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('item', kwargs={'name': self.name})

    class Meta:
        ordering = ['name']
        verbose_name = 'Продажа-Category'
        verbose_name_plural = 'Продажи-Category'

    def __str__(self):
        return self.name


'''4.Модель группировки проданных товаров по поставщикам'''


class SalesBySupplier(models.Model):
    code = models.DecimalField(
        max_digits=6, help_text="6 цифр", decimal_places=0)
    name = models.CharField(
        max_length=200, help_text="Не более 200 знаков", db_index=True, verbose_name='Категория')
    date = models.DateField(verbose_name='Дата',
                            help_text="'2022-08-18", null=True)
    weekday = models.PositiveIntegerField(
        verbose_name='День недели', null=True)
    revenue = models.DecimalField(
        max_digits=10, help_text="Не более 10 знаков", decimal_places=2, default=0, blank=True, null=True)
    gross_profit = models.DecimalField(
        max_digits=10, help_text="Не более 10 знаков", decimal_places=2, default=0, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('item', kwargs={'name': self.name})

    class Meta:
        ordering = ['name']
        verbose_name = 'Продажа-Supplier'
        verbose_name_plural = 'Продажи-Supplier'

    def __str__(self):
        return self.name

from django.db import models
from django.urls import reverse
from datetime import timedelta, date
from django.template.defaultfilters import slugify

# Create your models here.


# from decimal import Decimal


UNITS = (
    (None, 'Выбрать ед.изм.'),
    ('кг', 'кг'),
    ('л', 'л'),
    ('шт.', ' шт.'),
)

'''1.Модель поставщиков закупаемых товаров'''


class Supplier(models.Model):
    code = models.IntegerField(help_text="8 знаков", unique=True, null=True)
    name = models.CharField(
        max_length=200, help_text="Не более 200 знаков", db_index=True)
    slug = models.SlugField(max_length=255, verbose_name='Url')
    address = models.CharField(max_length=220)
    contact = models.CharField(max_length=250, null=True)
    created_date = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('supplier', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    def __str__(self):
        return self.name


'''1.1 Модель ЗАГРУЗКИ новых поставщиков закупаемых товаров'''


class SupplierLoading(models.Model):
    code = models.IntegerField(help_text="8 знаков", unique=True)
    name = models.CharField(
        max_length=200, help_text="Не более 200 знаков", db_index=True)
    address = models.CharField(max_length=220)
    contact = models.CharField(max_length=250, null=True)

    def get_absolute_url(self):
        return reverse('supplier', kwargs={'name': self.name})

    class Meta:
        ordering = ['name']
        verbose_name = 'Поставщик-Loading'
        verbose_name_plural = 'Поставщики-Loading'

    def __str__(self):
        return self.name


'''2.Модель покупателей товаров'''


class Buier(models.Model):
    code = models.IntegerField(help_text="8 знаков", null=True, unique=True)
    name = models.CharField(
        max_length=200, help_text="Не более 200 знаков", db_index=True)
    slug = models.SlugField(max_length=255, verbose_name='Url')
    address = models.CharField(max_length=220)
    contact = models.CharField(max_length=250, null=True)
    created_date = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('supplier', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'

    def __str__(self):
        return self.name


'''2.1 Модель ЗАГРУЗКИ новых покупателей товаров'''


class BuierLoading(models.Model):
    code = models.IntegerField(help_text="8 знаков", unique=True)
    name = models.CharField(
        max_length=200, help_text="Не более 200 знаков", db_index=True)
    address = models.CharField(max_length=220)
    contact = models.CharField(max_length=250, null=True)

    def get_absolute_url(self):
        return reverse('supplier', kwargs={'name': self.name})

    class Meta:
        ordering = ['name']
        verbose_name = 'Заказчик-Loading'
        verbose_name_plural = 'Заказчики-Loading'

    def __str__(self):
        return self.name


'''3. Модель категорий закупаемых товаров'''


class CategoryGoods(models.Model):
    code = models.DecimalField(
        max_digits=6, help_text="6 цифр", decimal_places=0, unique=True)
    name = models.CharField(
        max_length=200, help_text="Не более 200 знаков", db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, verbose_name='Slug', unique=True)
    created_date = models.DateField(
        auto_now_add=True, verbose_name='Создан', null=True)
    updated_date = models.DateField(
        auto_now=True,  verbose_name='Изменен', null=True)

    def get_absolute_url(self):
        return reverse('categoryitem', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


'''3.1 Модель ЗАГРУЗКИ новых категорий закупаемых товаров'''


class CategoryGoodsLoading(models.Model):
    code = models.IntegerField(help_text="6 цифр", unique=True)
    name = models.CharField(
        max_length=200, help_text="Не более 200 знаков", db_index=True, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse('categoryitem', kwargs={'name': self.name})

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория-Loading'
        verbose_name_plural = 'Категории-Loading'

    def __str__(self):
        return self.name


'''4. Модель закупаемых товаров'''


class Goods(models.Model):
    code = models.IntegerField(unique=True, help_text="12 знаков", null=True)
    name = models.CharField(
        max_length=200, help_text="Не более 200 знаков", db_index=True)
    category = models.ForeignKey(
        CategoryGoods, related_name='Goods', on_delete=models.CASCADE)
    supplier = models.ForeignKey(
        Supplier, related_name='Goods', on_delete=models.CASCADE)

    unit = models.CharField(
        max_length=10, help_text="Не более 10 знаков", choices=UNITS)
    unit_cost = models.DecimalField(
        max_digits=10, help_text="Не более 10 знаков", decimal_places=2)
    price = models.DecimalField(
        max_digits=10, help_text="Не более 10 знаков", decimal_places=2, default=10)
    description = models.TextField(blank=True, null=True)

    slug = models.SlugField(max_length=255, verbose_name='Url')
    delivery_time = models.IntegerField(verbose_name='Дней', null=True)
    supply_pack = models.IntegerField(
        verbose_name='Упаковка, ед.', null=True, default=1)
    pack_weight = models.FloatField(
        verbose_name='вес упаковки', blank=True, null=True)
    pack_length = models.FloatField(
        verbose_name='длина упаковки', blank=True, null=True)
    pack_width = models.FloatField(
        verbose_name='ширина упаковки', blank=True, null=True)
    pack_height = models.FloatField(
        verbose_name='высота упаковки', blank=True, null=True)

    created_date = models.DateField(
        auto_now_add=True, verbose_name='Создан', null=True)
    updated_date = models.DateField(
        auto_now=True,  verbose_name='Изменен', null=True)

    def get_absolute_url(self):
        return reverse('item', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['category', 'name']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


'''4.1 Модель ЗАГРУЗКИ новых закупаемых товаров'''


class GoodsLoading(models.Model):
    code = models.DecimalField(max_digits=12, unique=True, help_text="Не более 12 знаков",
                               decimal_places=0, null=True, verbose_name='Код')
    name = models.CharField(
        max_length=200, help_text="Не более 200 знаков", db_index=True)
    category = models.CharField(
        max_length=200, help_text="Не более 200 знаков",)
    supplier = models.CharField(
        max_length=200, help_text="Не более 200 знаков",)

    unit = models.CharField(
        max_length=50, help_text="Не более 50 знаков", choices=UNITS)
    unit_cost = models.DecimalField(
        max_digits=10, help_text="Не более 10 знаков", decimal_places=2)
    unit_price = models.DecimalField(
        max_digits=10, help_text="Не более 10 знаков", decimal_places=2, null=True)
    description = models.TextField(blank=True, null=True)
    delivery_time = models.IntegerField(
        verbose_name='Поставка, дней', null=True)
    supply_pack = models.IntegerField(verbose_name='Упаковка, ед.', null=True)
    pack_weight = models.FloatField(
        verbose_name='вес упаковки', blank=True, null=True)
    pack_length = models.FloatField(
        verbose_name='длина упаковки', blank=True, null=True)
    pack_width = models.FloatField(
        verbose_name='ширина упаковки', blank=True, null=True)
    pack_height = models.FloatField(
        verbose_name='высота упаковки', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('item', kwargs={'name': self.name})

    class Meta:
        ordering = ['category', 'name']
        verbose_name = 'Товар-Loading'
        verbose_name_plural = 'Товары-Loading'

    def __str__(self):
        return self.name
#

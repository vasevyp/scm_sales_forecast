# Generated by Django 4.1.7 on 2023-06-10 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Buier",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "code",
                    models.IntegerField(help_text="8 знаков", null=True, unique=True),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True, help_text="Не более 200 знаков", max_length=200
                    ),
                ),
                ("slug", models.SlugField(max_length=255, verbose_name="Url")),
                ("address", models.CharField(max_length=220)),
                ("contact", models.CharField(max_length=250, null=True)),
                ("created_date", models.DateField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "Заказчик",
                "verbose_name_plural": "Заказчики",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="BuierLoading",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.IntegerField(help_text="8 знаков", unique=True)),
                (
                    "name",
                    models.CharField(
                        db_index=True, help_text="Не более 200 знаков", max_length=200
                    ),
                ),
                ("address", models.CharField(max_length=220)),
                ("contact", models.CharField(max_length=250, null=True)),
            ],
            options={
                "verbose_name": "Заказчик-Loading",
                "verbose_name_plural": "Заказчики-Loading",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="CategoryGoods",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "code",
                    models.DecimalField(
                        decimal_places=0, help_text="6 цифр", max_digits=6, unique=True
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True,
                        help_text="Не более 200 знаков",
                        max_length=200,
                        verbose_name="Категория",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(max_length=255, unique=True, verbose_name="Slug"),
                ),
                (
                    "created_date",
                    models.DateField(
                        auto_now_add=True, null=True, verbose_name="Создан"
                    ),
                ),
                (
                    "updated_date",
                    models.DateField(auto_now=True, null=True, verbose_name="Изменен"),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="CategoryGoodsLoading",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.IntegerField(help_text="6 цифр", unique=True)),
                (
                    "name",
                    models.CharField(
                        db_index=True,
                        help_text="Не более 200 знаков",
                        max_length=200,
                        verbose_name="Категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория-Loading",
                "verbose_name_plural": "Категории-Loading",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="GoodsLoading",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "code",
                    models.DecimalField(
                        decimal_places=0,
                        help_text="Не более 12 знаков",
                        max_digits=12,
                        null=True,
                        unique=True,
                        verbose_name="Код",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True, help_text="Не более 200 знаков", max_length=200
                    ),
                ),
                (
                    "category",
                    models.CharField(help_text="Не более 200 знаков", max_length=200),
                ),
                (
                    "supplier",
                    models.CharField(help_text="Не более 200 знаков", max_length=200),
                ),
                (
                    "unit",
                    models.CharField(
                        choices=[
                            (None, "Выбрать ед.изм."),
                            ("кг", "кг"),
                            ("л", "л"),
                            ("шт.", " шт."),
                        ],
                        help_text="Не более 50 знаков",
                        max_length=50,
                    ),
                ),
                (
                    "unit_cost",
                    models.DecimalField(
                        decimal_places=2, help_text="Не более 10 знаков", max_digits=10
                    ),
                ),
                (
                    "unit_price",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="Не более 10 знаков",
                        max_digits=10,
                        null=True,
                    ),
                ),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "delivery_time",
                    models.IntegerField(null=True, verbose_name="Поставка, дней"),
                ),
                (
                    "supply_pack",
                    models.IntegerField(null=True, verbose_name="Упаковка, ед."),
                ),
                (
                    "pack_weight",
                    models.FloatField(
                        blank=True, null=True, verbose_name="вес упаковки"
                    ),
                ),
                (
                    "pack_length",
                    models.FloatField(
                        blank=True, null=True, verbose_name="длина упаковки"
                    ),
                ),
                (
                    "pack_width",
                    models.FloatField(
                        blank=True, null=True, verbose_name="ширина упаковки"
                    ),
                ),
                (
                    "pack_height",
                    models.FloatField(
                        blank=True, null=True, verbose_name="высота упаковки"
                    ),
                ),
            ],
            options={
                "verbose_name": "Товар-Loading",
                "verbose_name_plural": "Товары-Loading",
                "ordering": ["category", "name"],
            },
        ),
        migrations.CreateModel(
            name="Supplier",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "code",
                    models.IntegerField(help_text="8 знаков", null=True, unique=True),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True, help_text="Не более 200 знаков", max_length=200
                    ),
                ),
                ("slug", models.SlugField(max_length=255, verbose_name="Url")),
                ("address", models.CharField(max_length=220)),
                ("contact", models.CharField(max_length=250, null=True)),
                ("created_date", models.DateField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "Поставщик",
                "verbose_name_plural": "Поставщики",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="SupplierLoading",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.IntegerField(help_text="8 знаков", unique=True)),
                (
                    "name",
                    models.CharField(
                        db_index=True, help_text="Не более 200 знаков", max_length=200
                    ),
                ),
                ("address", models.CharField(max_length=220)),
                ("contact", models.CharField(max_length=250, null=True)),
            ],
            options={
                "verbose_name": "Поставщик-Loading",
                "verbose_name_plural": "Поставщики-Loading",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Goods",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "code",
                    models.IntegerField(help_text="12 знаков", null=True, unique=True),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True, help_text="Не более 200 знаков", max_length=200
                    ),
                ),
                (
                    "unit",
                    models.CharField(
                        choices=[
                            (None, "Выбрать ед.изм."),
                            ("кг", "кг"),
                            ("л", "л"),
                            ("шт.", " шт."),
                        ],
                        help_text="Не более 10 знаков",
                        max_length=10,
                    ),
                ),
                (
                    "unit_cost",
                    models.DecimalField(
                        decimal_places=2, help_text="Не более 10 знаков", max_digits=10
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2,
                        default=10,
                        help_text="Не более 10 знаков",
                        max_digits=10,
                    ),
                ),
                ("description", models.TextField(blank=True, null=True)),
                ("slug", models.SlugField(max_length=255, verbose_name="Url")),
                ("delivery_time", models.IntegerField(null=True, verbose_name="Дней")),
                (
                    "supply_pack",
                    models.IntegerField(
                        default=1, null=True, verbose_name="Упаковка, ед."
                    ),
                ),
                (
                    "pack_weight",
                    models.FloatField(
                        blank=True, null=True, verbose_name="вес упаковки"
                    ),
                ),
                (
                    "pack_length",
                    models.FloatField(
                        blank=True, null=True, verbose_name="длина упаковки"
                    ),
                ),
                (
                    "pack_width",
                    models.FloatField(
                        blank=True, null=True, verbose_name="ширина упаковки"
                    ),
                ),
                (
                    "pack_height",
                    models.FloatField(
                        blank=True, null=True, verbose_name="высота упаковки"
                    ),
                ),
                (
                    "created_date",
                    models.DateField(
                        auto_now_add=True, null=True, verbose_name="Создан"
                    ),
                ),
                (
                    "updated_date",
                    models.DateField(auto_now=True, null=True, verbose_name="Изменен"),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Goods",
                        to="dataset.categorygoods",
                    ),
                ),
                (
                    "supplier",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Goods",
                        to="dataset.supplier",
                    ),
                ),
            ],
            options={
                "verbose_name": "Товар",
                "verbose_name_plural": "Товары",
                "ordering": ["category", "name"],
            },
        ),
    ]
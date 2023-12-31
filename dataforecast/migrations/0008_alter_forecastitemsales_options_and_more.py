# Generated by Django 4.1.7 on 2023-07-28 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dataforecast", "0007_forecastitemsales_category"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="forecastitemsales",
            options={
                "ordering": ["code", "date"],
                "verbose_name": "Прогноз Продаж по Товарам",
                "verbose_name_plural": "Прогнозы Продаж по Товарам",
            },
        ),
        migrations.AlterField(
            model_name="forecastcategorysales",
            name="forecast",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                default=0,
                help_text="Не более 10 знаков",
                max_digits=20,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="forecastcategorysales",
            name="median_error",
            field=models.DecimalField(
                blank=True, decimal_places=2, default=0, max_digits=20, null=True
            ),
        ),
    ]

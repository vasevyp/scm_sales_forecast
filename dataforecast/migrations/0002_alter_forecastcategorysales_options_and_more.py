# Generated by Django 4.1.7 on 2023-07-07 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dataforecast", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="forecastcategorysales",
            options={
                "ordering": ["name"],
                "verbose_name": "Прогноз Продаж по Category",
                "verbose_name_plural": "Прогнозы Продаж по Category",
            },
        ),
        migrations.RenameField(
            model_name="forecastcategorysales",
            old_name="revenue",
            new_name="forecast",
        ),
    ]
# Generated by Django 4.1.7 on 2023-06-10 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("dataset", "0001_initial"),
        ("datasales", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sales",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="category_sale",
                to="dataset.goods",
            ),
        ),
    ]
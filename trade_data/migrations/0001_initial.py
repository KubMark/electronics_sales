# Generated by Django 4.2.1 on 2023-06-09 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Products",
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
                ("title", models.CharField(max_length=100, verbose_name="Название")),
                ("model", models.CharField(max_length=100, verbose_name="Модель")),
                (
                    "release_date",
                    models.DateTimeField(
                        blank=True,
                        null=True,
                        verbose_name="Дата выхода продукта на рынок",
                    ),
                ),
            ],
            options={
                "verbose_name": "Товар",
                "verbose_name_plural": "Товары",
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
                ("title", models.CharField(max_length=100, verbose_name="Название")),
                (
                    "types",
                    models.SmallIntegerField(
                        choices=[
                            (0, "Завод"),
                            (1, "Розничная сеть"),
                            (2, "Индивидуальный предпрениматель"),
                        ],
                        verbose_name="Тип звена",
                    ),
                ),
                (
                    "debt",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        max_digits=20,
                        verbose_name="Задолженность",
                    ),
                ),
                (
                    "create_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "email",
                    models.EmailField(max_length=50, unique=True, verbose_name="Email"),
                ),
                ("country", models.CharField(max_length=50, verbose_name="Страна")),
                ("city", models.CharField(max_length=50, verbose_name="Город")),
                (
                    "street",
                    models.CharField(max_length=100, verbose_name="Название улицы"),
                ),
                (
                    "building_number",
                    models.CharField(max_length=50, verbose_name="Номер дома"),
                ),
                (
                    "provider",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="trade_data.supplier",
                        verbose_name="Поставщик",
                    ),
                ),
            ],
            options={
                "verbose_name": "Поставщик",
                "verbose_name_plural": "Поставщики",
            },
        ),
    ]

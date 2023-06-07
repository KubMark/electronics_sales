from django.db import models


class Products(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100)
    model = models.CharField(verbose_name='Модель', max_length=100)
    release_date = models.DateTimeField(verbose_name='Дата выхода продукта на рынок', null=True, blank=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title


class Supplier(models.Model):
    """
    Supplier with hierarchy
    """
    TYPES = (
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предприниматель')
    )
    type = models.IntegerField(verbose_name='Тип компании', choices=TYPES)
    level = models.SmallIntegerField(verbose_name='Уровень в иерархии', default=0)
    title = models.CharField(verbose_name='Название', max_length=100)

    email = models.EmailField(verbose_name='Email', unique=True)
    country = models.CharField(verbose_name='Название страны', max_length=100)
    city = models.CharField(verbose_name='Название города', max_length=100)
    street = models.CharField(verbose_name='Название улицы', max_length=100)
    building_number = models.CharField(verbose_name='Номер дома', max_length=50)
    products = models.ManyToManyField(Products, verbose_name='Продукты')
    provider = models.ForeignKey(
        'self',
        verbose_name='Поставщик',
        on_delete=models.SET_NULL,
        related_name='Supplier',
        null=True,
        blank=True,)
    debt = models.DecimalField(
        verbose_name='Задолженность',
        max_digits=20,
        decimal_places=2,
        default=0)
    create_date = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    def __str__(self):
        return self.title

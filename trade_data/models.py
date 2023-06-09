from django.db import models


class Supplier(models.Model):
    TYPES = (
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предпрениматель',)
    )
    title = models.CharField(verbose_name='Название', max_length=100)
    types = models.SmallIntegerField(verbose_name='Тип звена', choices=TYPES)
    provider = models.ForeignKey('self', verbose_name='Поставщик', on_delete=models.SET_NULL, blank=True, null=True)
    debt = models.DecimalField(verbose_name='Задолженность', max_digits=20, decimal_places=2, default=0)
    create_date = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    email = models.EmailField(verbose_name='Email', unique=True, max_length=50)
    country = models.CharField(verbose_name='Страна', max_length=50)
    city = models.CharField(verbose_name='Город', max_length=50)
    street = models.CharField(verbose_name='Название улицы', max_length=100)
    building_number = models.CharField(verbose_name='Номер дома', max_length=50)

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    def __str__(self):
        return self.title


class Products(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100)
    model = models.CharField(verbose_name='Модель', max_length=100)
    release_date = models.DateTimeField(verbose_name='Дата выхода продукта на рынок', null=True, blank=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title




from django.db import models


class Supplier(models.Model):
    class Types(models.IntegerChoices):
        factory = 0, 'Завод'
        retail_network = 1, 'Розничная сеть'
        entrepreneur = 2, 'Индивидуальный предпрениматель'

    title = models.CharField(verbose_name='Название', max_length=100)
    types = models.SmallIntegerField(verbose_name='Тип звена', choices=Types.choices)
    provider = models.ForeignKey('self', verbose_name='Поставщик', on_delete=models.SET_NULL, blank=True, null=True)
    debt = models.DecimalField(verbose_name='Задолженность', max_digits=20, decimal_places=2, default=0)
    create_date = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    def __str__(self):
        return self.title


class Contacts(models.Model):
    provider = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    email = models.EmailField(verbose_name='Email', unique=True, max_length=50)
    country = models.CharField(verbose_name='Страна', max_length=50)
    city = models.CharField(verbose_name='Город', max_length=50)
    street = models.CharField(verbose_name='Название улицы', max_length=100)
    building_number = models.CharField(verbose_name='Номер дома', max_length=50)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.email


class Products(models.Model):
    provider = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Название', max_length=100)
    model = models.CharField(verbose_name='Модель', max_length=100)
    release_date = models.DateTimeField(verbose_name='Дата выхода продукта на рынок', null=True, blank=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title




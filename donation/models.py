from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Category(models.Model):
    """ Модель для Категории """
    name = models.CharField(max_length=100, verbose_name='Категории')
    description = models.CharField(max_length=150, unique=False, verbose_name='Описание')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class City(models.Model):
    title = models.CharField(max_length=40, unique=True, verbose_name='Город')

    class Meta:
        verbose_name = 'Городa'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Donation(models.Model):

    """ Модель для Объявлений """

    title = models.CharField(max_length=150, unique=False, verbose_name='Название')
    categoryId = models.ForeignKey(Category,  on_delete=models.CASCADE, blank=True, related_name='donation', verbose_name='Категория')
    description = models.CharField(max_length=150, unique=False, verbose_name='Описание')
    target = models.PositiveIntegerField(verbose_name='Нужная сумма')
    progress = models.PositiveIntegerField(verbose_name='Собранные средства')
    charityQty = models.PositiveIntegerField(verbose_name='Спонсоры')
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Город', default=None)
    owner = models.CharField(max_length=40, verbose_name='ФИО Получателя')
    phone_number = PhoneNumberField(blank=True, null=False, verbose_name="Tелефон")
    creation_date = models.DateField(verbose_name='Дата создания')
    end_date = models.DateField(verbose_name='Дата окончания')
    requisites = models.CharField(max_length=255, verbose_name='Реквизиты')
    is_active = models.BooleanField(verbose_name='Одобрено', default=False)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-id", "-creation_date"]
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


class DonationImage(models.Model):
    articleId = models.ForeignKey(Donation, on_delete=models.CASCADE, related_name='article_images',)
    image = models.ImageField(verbose_name='Фотография', null=True, blank=True)


class CategoryImage(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(verbose_name='Фотография', null=True, blank=True)


class Appeal(models.Model):
    phone_number = PhoneNumberField(blank=True, null=False, verbose_name="Tелефон")
    description = models.TextField(blank=True, verbose_name='Содержание')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата обращения')

    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = verbose_name


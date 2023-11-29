from django.db import models
from django.urls import reverse


class Item(models.Model):
    """
       Модель для представления товара.

       Поля:
       - name: Наименование товара (CharField).
       - description: Описание товара (TextField).
       - price: Цена товара (DecimalField).

       Методы:
       - str: Возвращает строковое представление товара (наименование).
       - get_absolute_url: Возвращает абсолютный URL для отображения страницы товара.
       """
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('get_item_page', args=[str(self.id)])

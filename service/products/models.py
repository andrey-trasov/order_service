from django.db import models


class Order(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    price = models.PositiveIntegerField(verbose_name="Цена")

    class Meta:
         verbose_name = "Заказ"
         verbose_name_plural = "Заказы"


    def __str__(self):
         return self.name

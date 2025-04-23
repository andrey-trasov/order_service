from django.db import models
from django.contrib.auth.models import User


class Tariff(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    price = models.PositiveIntegerField(verbose_name="Цена")

    class Meta:
         verbose_name = "Тариф"
         verbose_name_plural = "Тарифы"


    def __str__(self):
         return self.name


class UserSubscription (models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Пользователь")
    tariff = models.ForeignKey(Tariff, on_delete=models.PROTECT, verbose_name="Тариф")

    class Meta:
        verbose_name = "Подписка пользователя"
        verbose_name_plural = "Подписки пользователей"


    # def __str__(self):
    #     return self.user




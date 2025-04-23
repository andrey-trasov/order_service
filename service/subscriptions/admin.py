from django.contrib import admin

from subscriptions.models import Tariff, UserSubscription

@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin):
   list_display = ("id", "name", "price")

@admin.register(UserSubscription)
class UserSubscriptionAdmin(admin.ModelAdmin):
   list_display = ("id", "user", "tariff")
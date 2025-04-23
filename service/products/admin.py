from django.contrib import admin

from products.models import Order


@admin.register(Order)
class OrderSubscriptionAdmin(admin.ModelAdmin):
   list_display = ("id", "name", "price")
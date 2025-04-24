from django.contrib import admin

from user.models import User


@admin.register(User)
class UserSubscriptionAdmin(admin.ModelAdmin):
   list_display = ("id", "email")
from rest_framework.serializers import ModelSerializer

from subscriptions.models import Tariff, UserSubscription


class TariffSerializer(ModelSerializer):
   class Meta:
       model = Tariff
       fields = "__all__"

class UserSubscriptionSerializer(ModelSerializer):
   class Meta:
       model = UserSubscription
       fields = "__all__"
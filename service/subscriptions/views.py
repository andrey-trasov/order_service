from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from subscriptions.models import Tariff, UserSubscription
from subscriptions.serializers import TariffSerializer, UserSubscriptionSerializer


class TariffListAPIView(ListAPIView):
    """Возвразает список тарифов"""
    queryset = Tariff.objects.all()
    serializer_class = TariffSerializer
    permission_classes = (AllowAny,)  # открываем для анонимных пользователей

class UserSubscriptionViewSet(ModelViewSet):
    """Вьюсет для работы с подписками пользователя"""
    queryset = UserSubscription.objects.all()
    serializer_class = UserSubscriptionSerializer
    permission_classes = (AllowAny,)  # открываем для анонимных пользователей

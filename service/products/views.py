from rest_framework.viewsets import ModelViewSet

from products.models import Order
from products.serializers import OrderSerializer

from products.services import sending_telegram_message


class OrderViewSet(ModelViewSet):
    """Вьюсет для работы с Заказами"""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        serializer.save()
        tg_id = self.request.user.tg_id
        sending_telegram_message(tg_id)

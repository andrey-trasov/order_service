from rest_framework.viewsets import ModelViewSet

from products.models import Order
from products.serializers import OrderSerializer


class OrderViewSet(ModelViewSet):
    """Вьюсет для работы с Заказами"""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
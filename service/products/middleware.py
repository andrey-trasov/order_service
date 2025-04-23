from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from rest_framework import status
from rest_framework.response import Response

from subscriptions.models import UserSubscription


class SubscriptionCheckMiddleware(MiddlewareMixin):
    """
    Проверяет наличие подписки у пользователя для запросов к OrderViewSet.
    """

    def process_view(self, request, view_func, view_args, view_kwargs):
        """
        Выполняется перед вызовом view function.
        """

        # Проверяем, является ли view функцией OrderViewSet
        view_class = getattr(view_func, 'cls', None)  # Получаем класс viewset'а.  Для Function Based View это будет None.
        if view_class and view_class.__name__ == "OrderViewSet":
            # Получаем пользователя из запроса (предполагаем, что пользователь аутентифицирован)
            user = request.user

            # Проверяем, аутентифицирован ли пользователь
            if not user.is_authenticated:
                return Response({"error": "Authentication required."}, status=status.HTTP_401_UNAUTHORIZED)

            # Проверяем наличие подписки
            bull = UserSubscription.objects.filter(user=user).exists()

            if bull:
                # return Response(status=status.HTTP_400_BAD_REQUEST)
                return HttpResponse("Доступ запрещен", status=403)

            # Если подписка найдена, продолжаем выполнение запроса
            return None  # Важно: Вернуть None, чтобы запрос продолжил выполняться

        # Если это не OrderViewSet, продолжаем выполнение запроса
        return None
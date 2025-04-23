from django.urls import path
from rest_framework.routers import SimpleRouter
from subscriptions.apps import SubscriptionsConfig
from subscriptions.views import TariffListAPIView, UserSubscriptionViewSet

app_name = SubscriptionsConfig.name

router = SimpleRouter()
router.register('', UserSubscriptionViewSet)

urlpatterns = [
    path("lesson_tariff/", TariffListAPIView.as_view(), name="lesson_tariff"),
    # path("user_subscription/", UserSubscriptionViewSet.as_view(), name="user_subscription"),
    # path("lesson/<int:pk>/", LessonRetrieveAPIView.as_view(), name="lesson_detail"),
    # path("lesson_update/<int:pk>/", LessonUpdateAPIView.as_view(), name="lesson_update"),
    # path("lesson_delete/<int:pk>/", LessonDestroyAPIView.as_view(), name="lesson_delete"),
]

urlpatterns += router.urls
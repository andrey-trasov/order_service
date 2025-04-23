from django.urls import path
from rest_framework.routers import SimpleRouter
from products.apps import ProductsConfig
from products.views import OrderViewSet

app_name = ProductsConfig.name

router = SimpleRouter()
router.register('', OrderViewSet)

urlpatterns = []

urlpatterns += router.urls
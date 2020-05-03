from restaurant.viewsets import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('chef', ChefViewSet)
router.register('dish', DishViewSet)
router.register('customer', CustomerViewSet)
router.register('orders', OrdersViewSet)
router.register('payment', PaymentViewSet)

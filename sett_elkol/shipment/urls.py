from django.urls import path, include
from rest_framework import routers
from shipment.views import ShipmentViewSet

router = routers.DefaultRouter()
router.register('details/', ShipmentViewSet)


urlpatterns = [
    path('shipments/', include(router.urls)),
]
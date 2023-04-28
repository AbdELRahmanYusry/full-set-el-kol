from django.urls import path ,include
# from .views import payment_Details
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('payment/details/', views.payment_Details)

urlpatterns = [
    path("viewsets/", include(router.urls)),
]




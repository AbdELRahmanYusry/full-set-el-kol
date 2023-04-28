from django.shortcuts import render
from .models import payment_method
from .serializers import PaymentSerializer
from rest_framework import viewsets 

class payment_Details(viewsets.ModelViewSet):
    queryset = payment_method.objects.all()
    serializer_class = PaymentSerializer
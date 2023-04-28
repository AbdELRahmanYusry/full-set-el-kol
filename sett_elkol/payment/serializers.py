from rest_framework import serializers
from .models import payment_method

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = payment_method
        fields = ['card_number','Bank']
        
        
        
        
        
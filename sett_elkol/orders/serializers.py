from rest_framework import serializers
from orders.models import Order
from cart.serializers import CartItemSerializer

class OrderSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'items', 'status', 'total', 'created_at']
        read_only_fields = ['id', 'created_at']


# from rest_framework import serializers
# from .models import Order_Details , CartItem
# class CartItemSerializer(serializers.ModelSerializer):
#     meal = serializers.CharField(source = "meal.Meal.title")
#     customer_user = serializers.CharField(source = "customer.user") 
#     class Meta:
#         model = CartItem
#         fields = '__all__'
# class OrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Order_Details
#         fields = '__all__'
        
        





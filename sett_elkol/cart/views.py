from rest_framework import generics, mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from carts.models import CartItem
from carts.serializers import CartItemSerializer

class CartItemViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      generics.GenericAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        item_name = serializer.validated_data.get('item_name')
        if CartItem.objects.filter(user=self.request.user, item_name=item_name, status='incart').exists():
            return Response({'error': 'This item is already in your cart.'}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save(user=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



















# from django.shortcuts import render
# from rest_framework import viewsets, status
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from carts.models import CartItem
# from carts.serializers import CartItemSerializer

# class CartItemViewSet(viewsets.ModelViewSet):
#     queryset = CartItem.objects.all()
#     serializer_class = CartItemSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         return CartItem.objects.filter(user=self.request.user)

#     def perform_create(self, serializer):
#         item_name = serializer.validated_data.get('item_name')
#         if CartItem.objects.filter(user=self.request.user, item_name=item_name, status='incart').exists():
#             return Response({'error': 'This item is already in your cart.'}, status=status.HTTP_400_BAD_REQUEST)
#         serializer.save(user=self.request.user)

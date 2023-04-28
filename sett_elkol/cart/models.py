from django.db import models
from django.contrib.auth.models import User
from sett_elkol.meal.models import Meal

# User = get_user_model() 

class CartItem(models.Model):
    STATUS_CHOICES = (
        ('incart', 'In Cart'),
        ('outcart', 'Out of Cart')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal , related_name="meal_cart_item", on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=7, choices=STATUS_CHOICES, default='incart')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} x {self.item_name} ({self.user.username})"
   

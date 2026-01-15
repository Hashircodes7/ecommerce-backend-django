from django.db import models
from django.conf import settings
from products.models import Product
# Create your models here.
class Order(models.Model):
    status_choices=[
     ('pending','Pending'),
     ('paid','Paid'),
     ('shipped','Shipped'),
     ('delivered','Delivered'),
     ('cancelled','Cancelled')
    ]

    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='orders')
    total_price=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    status=models.CharField(max_length=20,choices=status_choices,default='pending')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}-{self.user.username}"
    

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items')
    product=models.ForeignKey(Product,on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"
    


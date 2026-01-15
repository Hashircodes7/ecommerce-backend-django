from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField(unique=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    desc=models.TextField(max_length=250)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    stock=models.PositiveIntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
    image=models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name
    


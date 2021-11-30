from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to="item_image")

    def __str__(self):
        return self.name


class Order(models.Model):
    total_order_cost = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"Order {self.pk}"

class OrderItem(models.Model):
    items = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default = 0)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    total_cost = models.DecimalField(decimal_places=2, max_digits=12)

    def __str__(self):
        return f"{self.items.name} order"


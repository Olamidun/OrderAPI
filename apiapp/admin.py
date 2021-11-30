from django.contrib import admin
from .models import Item, Order, OrderItem

# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'image', 'description']


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['quantity', 'total_cost'] 

 
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order)
admin.site.register(Item, ItemAdmin)
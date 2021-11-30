from .models import Item, Order, OrderItem
from rest_framework import serializers

from apiapp import models


class ListitemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class CreateOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    order_item= serializers.ListField(child=serializers.DictField(), write_only=True)
    total_order_cost = serializers.DecimalField( decimal_places=2, max_digits=12)

    def create(self, validated_data):
        order = Order.objects.create(total_order_cost=validated_data['total_order_cost'])

        item = validated_data['order_item']

        order_item_serializer = CreateOrderItemSerializer(data=item, many=True)
        order_item_serializer.is_valid(raise_exception=True)
        order_item_serializer.save(order_id=order.id)

        return order

class CreateOrderItemSerializer(serializers.Serializer):
    item_id = serializers.IntegerField(write_only=True)
    quantity = serializers.IntegerField()
    order_id = serializers.IntegerField(write_only=True, required=False)
    order = serializers.PrimaryKeyRelatedField(read_only=True)

    def create(self, validated_data):
        order = Order.objects.get(id=validated_data['order_id'])
        item = Item.objects.get(id=validated_data['item_id'])
        quantity = validated_data.get('quantity')
        price = float(quantity) * float(item.price)
        return OrderItem.objects.create(items=item, quantity=quantity, order=order, total_cost=price)
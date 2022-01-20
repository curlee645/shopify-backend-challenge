from rest_framework import serializers
from InventoryApp.models import Inventory

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ('purchaseId','productName','purchaseDate','supplier','productQuantity','costPerUnit','purchaseAmount')
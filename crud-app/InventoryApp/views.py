from django.shortcuts import render
from django.views.decorators.csrf  import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from InventoryApp.models import Inventory
from InventoryApp.serializers import InventorySerializer

from django.core.files.storage import default_storage

# Create your views here.
@csrf_exempt
def inventoryAPI(request, id = 0):
    if request.method =='GET':
        inventories = Inventory.objects.all()
        inventory_serializer = InventorySerializer(inventories, many=True)
        return JsonResponse(inventory_serializer.data, safe = False)
    elif request.method =='POST':
        inventory_data = JSONParser().parse(request)
        inventory_serializer = InventorySerializer(data = inventory_data)
        if inventory_serializer.is_valid():
            inventory_serializer.save()
            return JsonResponse('Added Successfully', safe = False)
        return JsonResponse('Failed to Add', safe = False)
    elif request.method =='PUT':
        inventory_data = JSONParser().parse(request)
        inventory = Inventory.objects.get(purchaseId = inventory_data['purchaseId'])
        inventory_serializer = InventorySerializer(inventory, data= inventory_data)
        if inventory_serializer.is_valid():
            inventory_serializer.save()
            return JsonResponse('Update Successfully', safe = False)
        return JsonResponse('Failed to Update', safe = False)
    elif request.method == 'DELETE':
        inventory = Inventory.objects.get(purchaseId = id)
        inventory.delete()
        return JsonResponse("Delete Successfully",safe = False)


@csrf_exempt
def SaveFile(request):
    file = request.FILES('file')
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe = False)
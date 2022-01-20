from django.conf.urls import url
from InventoryApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
    url(r'^inventory$', views.inventoryAPI),
    url(r'^inventory/([0-9]+)$', views.inventoryAPI),

    url(r'^inventory/savefile', views.SaveFile) 

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
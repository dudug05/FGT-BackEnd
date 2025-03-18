from rest_framework.viewsets import ModelViewSet

from core.models import Supplier
from core.serializers import SupplierSerializer

class SupplierViewSet(ModelViewSet):
   queryset = Supplier.objects.all()
   serializer_class = SupplierSerializer
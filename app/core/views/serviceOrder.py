from rest_framework.viewsets import ModelViewSet

from core.models import ServiceOrder
from core.serializers import ServiceOrderSerializer


class ServiceOrderViewSet(ModelViewSet):
    queryset = ServiceOrder.objects.all()
    serializer_class = ServiceOrderSerializer
from rest_framework.viewsets import ModelViewSet

#from rest_framework.permissions import IsAuthenticated #Teste permissão

from core.models import Customer
from core.serializers import CustomerSerializer


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    #permission_classes = [IsAuthenticated] #teste permissão
    
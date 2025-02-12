from rest_framework.viewsets import ModelViewSet

from core.models import Financa
from core.serializers import FinancaSerializer


class FinancaViewSet(ModelViewSet):
    queryset = Financa.objects.all()
    serializer_class = FinancaSerializer
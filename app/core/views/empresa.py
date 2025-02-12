from rest_framework.viewsets import ModelViewSet

from core.models import Empresa
from core.serializers import EmpresaSerializer


class EmpresaViewSet(ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
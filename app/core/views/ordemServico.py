from rest_framework.viewsets import ModelViewSet

from core.models import OrdemServico
from core.serializers import OrdemServicoSerializer


class OrdemServicoViewSet(ModelViewSet):
    queryset = OrdemServico.objects.all()
    serializer_class = OrdemServicoSerializer
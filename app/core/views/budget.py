from rest_framework.viewsets import ModelViewSet

from rest_framework.permissions import IsAuthenticated

from core.models import Budget
from core.serializers import BudgetSerializer


class BudgetViewSet(ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    permission_classes = [IsAuthenticated]
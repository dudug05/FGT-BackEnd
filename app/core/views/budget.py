from rest_framework.viewsets import ModelViewSet

from core.models import Budget
from core.serializers import BudgetSerializer


class BudgetViewSet(ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
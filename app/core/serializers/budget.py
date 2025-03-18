from rest_framework.serializers import ModelSerializer

from core.models import Budget


class BudgetSerializer(ModelSerializer):
    class Meta:
        model = Budget
        fields = "__all__"
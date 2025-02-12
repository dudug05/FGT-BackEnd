from rest_framework.serializers import ModelSerializer

from core.models import Financa


class FinancaSerializer(ModelSerializer):
    class Meta:
        model = Financa
        fields = "__all__"
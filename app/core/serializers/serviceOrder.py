from rest_framework.serializers import ModelSerializer

from core.models import ServiceOrder


class ServiceOrderSerializer(ModelSerializer):
    class Meta:
        model = ServiceOrder
        fields = "__all__"
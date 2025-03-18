from rest_framework.viewsets import ModelViewSet

from core.models import Employee
from core.serializers import EmployeeSerializer


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter 

from core.views import UsuarioViewSet  
from core.views import CustomerViewSet
from core.views import ServiceViewSet
from core.views import ProductViewSet
from core.views import EmployeeViewSet
from core.views import BudgetViewSet
from core.views import ServiceOrderViewSet
from core.views import SupplierViewSet


router = DefaultRouter()
router.register(r"usuario", UsuarioViewSet)
router.register(r"customer", CustomerViewSet)
router.register(r"service", ServiceViewSet)
router.register(r"product", ProductViewSet)
router.register(r"employee", EmployeeViewSet)
router.register(r"budget", BudgetViewSet)
router.register(r"serviceorder", ServiceOrderViewSet)
router.register(r"supplier", SupplierViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  
]

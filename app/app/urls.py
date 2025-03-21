from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter 
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


from core.views import UserViewSet  
from core.views import CustomerViewSet
from core.views import ServiceViewSet
from core.views import ProductViewSet
from core.views import EmployeeViewSet
from core.views import BudgetViewSet
from core.views import ServiceOrderViewSet
from core.views import SupplierViewSet


router = DefaultRouter()
router.register(r"user", UserViewSet)
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
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
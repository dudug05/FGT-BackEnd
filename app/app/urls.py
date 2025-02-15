from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter 

from core.views import UsuarioViewSet  
from core.views import EmpresaViewSet
from core.views import ClienteViewSet
from core.views import FinancaViewSet
from core.views import ServicoViewSet
from core.views import ProdutoViewSet
from core.views import PedidoViewSet
from core.views import ItemPedidoViewSet


router = DefaultRouter()
router.register(r"usuario", UsuarioViewSet)
router.register(r"empresa", EmpresaViewSet)
router.register(r"cliente", ClienteViewSet)
router.register(r"financa", FinancaViewSet)
router.register(r"servico", ServicoViewSet)
router.register(r"produto", ProdutoViewSet)
router.register(r"pedido", PedidoViewSet)
router.register(r"itempedido", ItemPedidoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  
]

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter 

from core.views import UsuarioViewSet  
from core.views import FornecedorViewSet
from core.views import ClienteViewSet
from core.views import ServicoViewSet
from core.views import ProdutoViewSet
from core.views import FuncionarioViewSet
from core.views import OrcamentoViewSet
from core.views import OrdemServicoViewSet


router = DefaultRouter()
router.register(r"usuario", UsuarioViewSet)
router.register(r"fornecedor", FornecedorViewSet)
router.register(r"cliente", ClienteViewSet)
router.register(r"servico", ServicoViewSet)
router.register(r"produto", ProdutoViewSet)
router.register(r"funcionario", FuncionarioViewSet)
router.register(r"orcamento", OrcamentoViewSet)
router.register(r"ordemservico", OrdemServicoViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  
]

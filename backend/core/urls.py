from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet, TransacaoViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'transacoes', TransacaoViewSet)

urlpatterns = router.urls
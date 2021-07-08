from django.contrib import admin
from django.urls import path,include
from api.views import ClientesViewSet, EmprestimosViewSet, ListaEmprestimosClienteViewSet, ListaClientesViewSet, StartValidator, ConsultaViewSet, ConsultaTicketViewSet
from rest_framework import routers
from api import views
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API",
      default_version='v1',
      description="Api para consulta de crédito",
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


router = routers.DefaultRouter()
router.register('clientes', ClientesViewSet, basename='Clientes')
router.register('emprestimos', EmprestimosViewSet, basename='Emprestimos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls) ),
    path('clientes/<int:pk>/emprestimos', ListaEmprestimosClienteViewSet.as_view()),
    path('clientes/<int:pk>/emprestar/', csrf_exempt(views.StartValidator.as_view())),
    path('clientes/<int:pk>/consultar', ConsultaViewSet.as_view()),
    path('clientes/<int:pk>/consultar/<uuid:uuid>', ConsultaTicketViewSet.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
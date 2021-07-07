from django.contrib import admin
from django.urls import path,include
from api.views import ClientesViewSet, EmprestimosViewSet, ListaEmprestimosClienteViewSet, ListaClientesViewSet, StartValidator
from rest_framework import routers
from api import views
from django.views.decorators.csrf import csrf_exempt

router = routers.DefaultRouter()
router.register('clientes', ClientesViewSet, basename='Clientes')
router.register('emprestimos', EmprestimosViewSet, basename='Emprestimos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls) ),
    path('clientes/<int:pk>/emprestimos', ListaEmprestimosClienteViewSet.as_view()),
    path('clientes/<int:pk>/emprestar/', csrf_exempt(views.StartValidator.as_view()))
]
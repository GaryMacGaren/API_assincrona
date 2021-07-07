from django.contrib import admin
from django.urls import path,include
# from django.conf import settings
# from escola.views import AlunosViewSet, CursosViewSet, MatriculaViewSet, ListaMatriculasAluno, ListaAlunosMatriculados
from api.views import ClientesViewSet, EmprestimosViewSet, ListaEmprestimosViewSet, ListaEmprestimosClienteViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('clientes', ClientesViewSet, basename='Clientes')
router.register('emprestimos', EmprestimosViewSet, basename='Emprestimos')
# router.register('matriculas', MatriculaViewSet, basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls) ),
    path('clientes/<int:pk>/emprestimos', ListaEmprestimosClienteViewSet.as_view()),
    path('emprestimos/<int:pk>', ListaEmprestimosViewSet.as_view())
]
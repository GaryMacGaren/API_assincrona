from rest_framework import viewsets, generics
# from escola.models import Aluno, Curso, Matricula
# from escola.serializer import AlunoSerializerV2 ,AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunosMatriculadosSerializer
from api.models import Cliente, Emprestimo
from api.serializer import ClienteSerializer, EmprestimoSerializer, ListaClientesSerializer, ListaEmprestimosSerializer, ListaEmprestimosClienteSerializer
# from rest_framework.response import Response
# from django.views.decorators.cache import cache_page


class ClientesViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    http_method_names = ['get', 'post', 'put']
    # def get_serializer_class(self):
    #     if self.request.version == 'v2':
    #         return AlunoSerializerV2
    #     else:
    #         return AlunoSerializer

class EmprestimosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer
    http_method_names = ['get', 'post', 'put']

class ListaClientesViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = Cliente.objects.filter(pk=self.kwargs['pk'])
        return queryset

    serializer_class = ListaClientesSerializer

class ListaEmprestimosClienteViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = Emprestimo.objects.filter(cliente_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListaEmprestimosClienteSerializer


class ListaEmprestimosViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = Emprestimo.objects.filter(ticket=self.kwargs['ticket'])
        return queryset

    serializer_class = ListaEmprestimosSerializer



from rest_framework import viewsets, generics
from api.models import Cliente, Emprestimo
from api.serializer import ClienteSerializer, EmprestimoSerializer, ListaClientesSerializer, ListaEmprestimosClienteSerializer
from rest_framework.response import Response
import datetime


class ClientesViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    http_method_names = ['get', 'post', 'put']

class EmprestimosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer
    http_method_names = ['get', 'post']


class ListaClientesViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = Cliente.objects.filter(pk=self.kwargs['pk'])
        return queryset

    serializer_class = ListaClientesSerializer

class ListaEmprestimosClienteViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = Emprestimo.objects.filter(cliente__id=self.kwargs['pk'])
        return queryset

    serializer_class = ListaEmprestimosClienteSerializer


class StartValidator(generics.CreateAPIView):
    def post(self, request, **kwargs):
        if request.method == "POST":
            cliente = Cliente.objects.get(id=kwargs['pk'])
            idade = datetime.datetime.now().year - cliente.data_nascimento.year #TODO melhorar essa logica
            valor = float(request.data['valor'])
            return Response('ticket 100')

    def get(self, request, **kwargs):
        if request.method == "GET":
            return Response('GET agora permitido')

    serializer_class = EmprestimoSerializer



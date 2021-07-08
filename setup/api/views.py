from rest_framework import viewsets, generics
from api.models import Cliente, Emprestimo
from api.serializer import ClienteSerializer, EmprestimoSerializer, ListaClientesSerializer, ListaEmprestimosClienteSerializer
from rest_framework.response import Response
from setup.celery import validator
import datetime

class ClientesViewSet(viewsets.ModelViewSet):
    """Exibe todos os clientes na base de dados"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    http_method_names = ['get', 'post', 'put']

class EmprestimosViewSet(viewsets.ModelViewSet):
    """Exibe todos os emprestimos na base de dados"""
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer
    http_method_names = ['get']


class ListaClientesViewSet(generics.ListAPIView):
    """Lista um determinado cliente pelo id"""
    def get_queryset(self):
        queryset = Cliente.objects.filter(pk=self.kwargs['pk'])
        return queryset

    serializer_class = ListaClientesSerializer

class ListaEmprestimosClienteViewSet(generics.ListAPIView):
    """Lista todos os emprestimos realizados por um determinado cliente"""
    def get_queryset(self):
        queryset = Emprestimo.objects.filter(cliente__id=self.kwargs['pk'])
        return queryset

    serializer_class = ListaEmprestimosClienteSerializer


class StartValidator(generics.CreateAPIView):
    """Inicia a chamada assincrona do Validator"""
    def post(self, request, **kwargs):
        if request.method == "POST":
            cliente = Cliente.objects.get(id=kwargs['pk'])
            idade = datetime.datetime.now().year - cliente.data_nascimento.year #TODO melhorar essa logica
            valor = float(request.data['valor'])
            emprestimo = Emprestimo.objects.create(valor=valor, cliente_id=cliente.id)
            if emprestimo:
                print('objeto criado com sucesso')
                resposta = validator.delay(idade=str(idade), valor=str(valor), id_cliente=kwargs['pk']).id
            else:
                resposta = 'objeto nao pode ser criado'
            return Response(resposta)


    def get(self, request, **kwargs):
        if request.method == "GET":
            return Response()

    serializer_class = EmprestimoSerializer

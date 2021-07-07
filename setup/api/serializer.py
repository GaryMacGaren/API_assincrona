from rest_framework import serializers
from api.models import Cliente, Emprestimo

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class EmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprestimo
        fields = ['valor','cliente']

class ListaClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nome', 'rg']

class ListaEmprestimosClienteSerializer(serializers.ModelSerializer):
    # emprestimo_nome = serializers.ReadOnlyField(source='emprestimo.cliente.nome')
    # valor = serializers.ReadOnlyField(source='valor')
    class Meta:
        model = Emprestimo
        fields = '__all__'

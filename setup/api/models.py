from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()

    def __str__(self):
        return f'nome: {self.nome} - rg: {self.rg}'

class Emprestimo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    ticket = models.SlugField(max_length=40)
    data = models.DateField(auto_now=True)
    aprovado = models.BooleanField(default=False)

    def __str__(self):
        return f'nome: {self.cliente.nome} - valor: {self.valor}'

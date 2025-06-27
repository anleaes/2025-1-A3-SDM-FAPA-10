from django.db import models
from cliente.models import Cliente

# Create your models here.

class ServicosExtra(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nome

class ItemCliente(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servico = models.ForeignKey(ServicosExtra, on_delete=models.CASCADE)
    data_adicao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cliente.nome} - {self.servico.nome}"
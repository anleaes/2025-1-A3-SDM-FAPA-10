from django.db import models
from cliente.models import Cliente
from nutricionista.models import Nutricionista

# Create your models here.

class Dieta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nutricionista = models.ForeignKey(Nutricionista, on_delete=models.SET_NULL, null=True)
    objetivo = models.CharField(max_length=200)
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)
    class Meta:
        verbose_name = 'Dieta'
        verbose_name_plural = 'Dietas'
        ordering =['id']

class PlanoAlimentar(models.Model):
    dieta = models.ForeignKey(Dieta, on_delete=models.CASCADE, related_name='planos')
    alimento = models.ForeignKey('alimento.Alimento', on_delete=models.CASCADE)
    refeicao = models.CharField(max_length=50)  # Café, Almoço, etc.
    quantidade = models.DecimalField(max_digits=6, decimal_places=2)
    horario = models.TimeField()


    def __str__(self):
        return f"{self.refeicao} - {self.alimento.nome}"
from django.db import models
from cliente.models import Cliente
from personal.models import Personal 
from exercicio.models import Exercicio 
# Create your models here.

class Treino(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    personal = models.ForeignKey(Personal, on_delete=models.SET_NULL, null=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data_criacao = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Treino'
        verbose_name_plural = 'Treinos'
        ordering =['id']

    def __str__(self):
        return self.nome
    


class TreinoExercicio(models.Model):
    treino = models.ForeignKey(Treino, on_delete=models.CASCADE, related_name='exercicios')
    exercicio = models.ForeignKey(Exercicio, on_delete=models.CASCADE)
    ordem = models.IntegerField()
    series = models.IntegerField()
    repeticoes = models.IntegerField()  
    
    def __str__(self):
        return f"{self.exercicio.nome} - {self.treino.nome}"
    
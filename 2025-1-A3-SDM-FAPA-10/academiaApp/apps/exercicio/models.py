from django.db import models

# Create your models here.

class Exercicio(models.Model):
    nome = models.CharField(max_length=100)
    grupo_muscular = models.CharField(max_length=100)
    duracao = models.TimeField(max_length=100, blank=True)
    equipamento = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = 'Exercicio'
        verbose_name_plural = 'Exercicios'
        ordering =['id']

    def __str__(self):
        return self.nome
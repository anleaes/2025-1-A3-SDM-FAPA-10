from django.db import models

# Create your models here.

class Exercicio(models.Model):
    name = models.CharField('Nome', max_length=50)
    descricao = models.TextField('Descriçao', max_length=100)

    class Meta:
        verbose_name = 'Exercicio'
        verbose_name_plural = 'Exercicios'
        ordering =['id']

    def __str__(self):
        return self.name
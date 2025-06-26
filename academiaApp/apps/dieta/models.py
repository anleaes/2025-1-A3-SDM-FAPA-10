from django.db import models

# Create your models here.

class Dieta(models.Model):
    name = models.CharField('Nome', max_length=50)
    descricao = models.TextField('Descriçao', max_length=100)

    class Meta:
        verbose_name = 'Dieta'
        verbose_name_plural = 'Dietas'
        ordering =['id']

    def __str__(self):
        return self.name
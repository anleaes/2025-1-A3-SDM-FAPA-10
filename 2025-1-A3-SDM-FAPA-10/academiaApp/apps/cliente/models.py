from django.db import models

# Create your models here.

class Cliente(models.Model):
    name = models.CharField('Nome', max_length=50)
    sobrenome = models.TextField('Sobrenome', max_length=100)
    endereco = models.TextField('endereço', max_length=100)
    cpf = models.TextField('cpf', max_length=100)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering =['id']

    def __str__(self):
        return self.name
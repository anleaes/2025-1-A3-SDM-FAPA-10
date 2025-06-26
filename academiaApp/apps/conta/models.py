from django.db import models

# Create your models here.

class Conta(models.Model):
    Usuario = models.TextField('Usuario', max_length=50)
    Senha= models.TextField('Senha', max_length=100)
    
    class Meta:
        verbose_name = 'Conta'
        verbose_name_plural = 'Contas'
        ordering =['id']

    def __str__(self):
        return self.name
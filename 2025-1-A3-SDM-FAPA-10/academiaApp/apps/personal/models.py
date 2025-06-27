from django.db import models

# Create your models here.

class Personal(models.Model):
    nome = models.CharField(max_length=100)
    cref = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    
    class Meta:
        verbose_name = 'Personal'
        verbose_name_plural = 'Personais'
        ordering =['id']

    def __str__(self):
        return self.nome
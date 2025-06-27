from django.db import models

# Create your models here.

class Nutricionista(models.Model):
    nome = models.CharField(max_length=100)
    crn = models.CharField(max_length=20, unique=True)
    especialidade = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    class Meta:
        verbose_name = 'Nutricionista'
        verbose_name_plural = 'Nutricionistas'
        ordering =['id']

    def __str__(self):
        return self.name
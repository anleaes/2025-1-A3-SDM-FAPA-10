from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField("Nome Completo", max_length=200)
    sobrenome = models.CharField("Sobrenome", max_length=200)
    rua = models.CharField("Rua / Endereço", max_length=255)
    email = models.EmailField("Endereço de Email", unique=True)
    
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('N', 'Não Especificado'),
    ]
    sexo = models.CharField("Sexo", max_length=1, choices=SEXO_CHOICES, default='N')

    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['id']

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"
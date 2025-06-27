from django.db import models

# Create your models here.

class Alimento(models.Model):
    nome = models.CharField(max_length=100)
    calorias = models.DecimalField(max_digits=6, decimal_places=2)
    proteinas = models.DecimalField(max_digits=5, decimal_places=2)
    carboidratos = models.DecimalField(max_digits=5, decimal_places=2)
    gorduras = models.DecimalField(max_digits=5, decimal_places=2)
    
    class Meta:
        verbose_name = 'Alimento'
        verbose_name_plural = 'Alimentos'
        ordering =['id']

    def __str__(self):
        return self.nome
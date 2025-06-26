from django.db import models

# Create your models here.

class Alimento(models.Model):
    nome = models.TextField('Alimento', max_length=50)
    tipoAlimento = models.TextField('tipo de alimento', max_length=100)
    
    class Meta:
        verbose_name = 'Alimento'
        verbose_name_plural = 'Alimentos'
        ordering =['id']

    def __str__(self):
        return self.name
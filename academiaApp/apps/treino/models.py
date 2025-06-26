from django.db import models

# Create your models here.

class Treino(models.Model):
    exercicio = models.TextField('Exercicio', max_length=50)
    grupoMuscular = models.TextField('Grupo Muscular', max_length=100)
    
    class Meta:
        verbose_name = 'Personal'
        verbose_name_plural = 'Personais'
        ordering =['id']

    def __str__(self):
        return self.name
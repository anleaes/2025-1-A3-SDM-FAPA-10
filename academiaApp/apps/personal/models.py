from django.db import models

# Create your models here.

class Personal(models.Model):
    name = models.CharField('Nome', max_length=50)
    sobrenome = models.TextField('sobrenome', max_length=100)
    
    class Meta:
        verbose_name = 'Personal'
        verbose_name_plural = 'Personais'
        ordering =['id']

    def __str__(self):
        return self.name
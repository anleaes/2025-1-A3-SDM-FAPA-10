from django.db import models

# Create your models here.

class ServicosExtra(models.Model):
    name = models.CharField('Nome', max_length=50)
    preço = models.TextField('Valor', max_length=100)
    
    class Meta:
        verbose_name = 'ServicosExtra'
        verbose_name_plural = 'ServicosExtras'
        ordering =['id']

    def __str__(self):
        return self.name
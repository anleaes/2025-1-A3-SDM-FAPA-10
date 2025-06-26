from django.db import models

# Create your models here.


class Cliente(models.Model):
    primeiro_nome = models.CharField("Primeiro-Nome", max_length=150)
    segundo_nome = models.CharField("Segundo-Nome", max_length=150)
    endereco = models.CharField("Endereco", max_length=150)
    email = models.EmailField("Email", null=False, blank=False)
    GENEROS = (("M", "Masculino"), ("F", "Feminino"), ("O", "Outro"))
    genero = models.CharField("Genenro", max_length=1, choices=GENEROS)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ["id"]

    def __str__(self):
        return self.primeiro_nome


    

    def __str__(self):
        return self.socialnetwork.name

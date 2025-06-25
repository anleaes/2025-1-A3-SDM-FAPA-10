from django.db import models
from django.contrib.auth.models import User

# Create your models here.





class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()
    objetivo = models.TextField(blank=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    USER_TYPES = (
        ('aluno', 'Aluno'),
        ('personal', 'Personal Trainer'),
        ('nutri', 'Nutricionista'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
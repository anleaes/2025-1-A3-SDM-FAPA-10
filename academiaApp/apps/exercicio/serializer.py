from .models import Exercicio
from rest_framework import serializers

class ExercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercicio 
        fields = '__all__'
        
        # Para chamar todos os atributos:
        # fields = '__all__'
        
        # Para chamar somentes os atributos de interesse:
        # fields = ['id','created_on', 'updated_on', 'name', 'description']
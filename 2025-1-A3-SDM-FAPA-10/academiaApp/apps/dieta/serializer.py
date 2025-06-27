from .models import Dieta
from rest_framework import serializers

class DietaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dieta 
        fields = '__all__'
        
        # Para chamar todos os atributos:
        # fields = '__all__'
        
        # Para chamar somentes os atributos de interesse:
        # fields = ['id','created_on', 'updated_on', 'name', 'description']
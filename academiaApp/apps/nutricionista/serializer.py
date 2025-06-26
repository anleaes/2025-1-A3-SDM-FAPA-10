from .models import Nutricionista
from rest_framework import serializers

class NutricionistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nutricionista
        fields = '__all__'
        
        # Para chamar todos os atributos:
        # fields = '__all__'
        
        # Para chamar somentes os atributos de interesse:
        # fields = ['id','created_on', 'updated_on', 'name', 'description']
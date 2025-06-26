from .models import ServicosExtra
from rest_framework import serializers

class ServicosExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicosExtra
        fields = '__all__'
        
        # Para chamar todos os atributos:
        # fields = '__all__'
        
        # Para chamar somentes os atributos de interesse:
        # fields = ['id','created_on', 'updated_on', 'name', 'description']
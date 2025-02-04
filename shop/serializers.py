from rest_framework import serializers
from .models import Shirt
from .models import Pants
from .models import Shorts
from .models import Cap

class ShirtSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Shirt  
        fields = '__all__'

class PantsSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Pants  
        fields = '__all__'
        
class ShortsSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Shorts  
        fields = '__all__'
        
class CapSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Cap  
        fields = '__all__'
        

from rest_framework import serializers
from .models import FcMallProduct

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = FcMallProduct
        fields = '__all__'
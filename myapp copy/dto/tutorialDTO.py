from rest_framework import serializers 
from myapp.models.productModel import ProductModel
 
 
class tutorialDTO(serializers.ModelSerializer):
 
    class Meta:
        model = ProductModel
        fields = ('id',
                  'name',
                  'description',
                  'price')
from django.shortcuts import get_object_or_404
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from myapp.models.productModel import ProductModel
from myapp.dto.productDTO import productDTO 
from myapp.response.helper import BaseResponse

@api_view(['GET', 'PUT', 'DELETE'])
def getProducts(request):
    if request.method == 'GET':
        products = ProductModel.objects.all()
        response = productDTO(products, many=True)
        return BaseResponse('success', 'Successfully fetched products', response.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        product = get_object_or_404(ProductModel, id=data.get('id'))

        product.name = data.get('name', product.name)
        product.description = data.get('description', product.description)
        product.price = data.get('price', product.price)
        product.save()

        response = productDTO(product)

        return BaseResponse('success', 'Successfully updated product', response.data)

    elif request.method == 'DELETE':
        data = JSONParser().parse(request)
        product = get_object_or_404(ProductModel, id=data.get('id'))

        product.delete()

        return BaseResponse('success', 'Successfully deleted product', None)

@api_view(['GET'])
def getProductById(request, product_id):
    product = get_object_or_404(ProductModel, id=product_id)
    response = productDTO(product)
    
    return BaseResponse('success', 'Successfully fetched product', response.data)
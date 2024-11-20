from django.http import JsonResponse,HttpResponse
import json
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer

@api_view(['GET'])
def api_home(request,*args,**kwargs):

    instance = Product.objects.all().order_by("?").first()

    data={}

    # if model_data:
    #    data= model_to_dict(model_data,fields=['id','title','price','sale_price'])
    
    if instance:
        data = ProductSerializer(instance)
        print("#######serializer object########")
        print(data)
        data= data.data
        print("#######serializer object.data###")
        print(data)
  
    return Response(data)





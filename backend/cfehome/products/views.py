from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset= Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self,serializer):

        
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')

        if content is None:
            content= title

        serializer.save(content=content)


class ProductDetailAPIView(generics.RetrieveAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer 


#class ProductListAPIView(generics.RetrieveAPIView):

#    queryset = Product.objects.all()
#    serializer_class = ProductSerializer 


@api_view(['GET','POST'])
def product_alt_view(request,pk=None,*args,**kwargs):
    method= request.method

    if method == "GET":
        if pk != None:
            obj = get_object_or_404(Product,pk=pk)
            data = ProductSerializer(obj,many=False).data

            return Response(data)
         

        queryset = Product.objects.all()
        data = ProductSerializer(queryset,many=True).data
        return Response(data)
        

    elif method == "POST":
            
        serializer = ProductSerializer(data=request.data)


        if serializer.is_valid(raise_exception=True):

            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content')

            if content is None:
                content= title

            serializer.save(content=content)
            
            return Response(serializer.data)
   
        # return Response({"invalid":"not good data"},status=400)


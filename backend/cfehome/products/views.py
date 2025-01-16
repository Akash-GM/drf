from rest_framework import generics, permissions, authentication
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404
from api.permissions import IsStaffEditorPermissions
from api.authentication import TokenAuthentication
from api.mixins import StaffEditorPermissionMixin, UserQuerySetMixin


class ProductListCreateAPIView(
    UserQuerySetMixin, StaffEditorPermissionMixin, generics.ListCreateAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    allow_staff_view = True

    def perform_create(self, serializer):
        email = serializer.validated_data.pop("email")
        print(serializer.validated_data)
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content")

        if content is None:
            content = title
        print("no i say no no no no")
        serializer.save(user=self.request.user, content=content)

    # def get_queryset(self, *args, **kwargs):
    #     qs = super().get_queryset(*args, **kwargs)
    #     request = self.request
    #     user = request.user
    #     if not user.is_authenticated:
    #         return Product.objects.none()
    #     print("what came from get queryset ")
    #     return qs.filter(user=request.user)


class ProductDetailAPIView(
    UserQuerySetMixin, StaffEditorPermissionMixin, generics.RetrieveAPIView
):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# class ProductListAPIView(generics.RetrieveAPIView):

#    queryset = Product.objects.all()
#    serializer_class = ProductSerializer


class ProductUpdateAPIView(
    UserQuerySetMixin, StaffEditorPermissionMixin, generics.UpdateAPIView
):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


class ProductDestroyAPIView(
    UserQuerySetMixin, StaffEditorPermissionMixin, generics.DestroyAPIView
):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


@api_view(["GET", "POST"])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method == "GET":
        if pk != None:
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data

            return Response(data)

        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)

    elif method == "POST":

        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):

            title = serializer.validated_data.get("title")
            content = serializer.validated_data.get("content")

            if content is None:
                content = title

            serializer.save(content=content)

            return Response(serializer.data)

        # return Response({"invalid":"not good data"},status=400)

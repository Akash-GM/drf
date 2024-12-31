from rest_framework import viewsets
from rest_framework import mixins
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    this is the product view set
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"


class ProductGenericViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    """
    this is the generic product view set
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"


product_list_view = ProductGenericViewSet.as_view({"get": "list"})
product_detail_view = ProductGenericViewSet.as_view(
    {"get": "retrieve"}
)  # now these can be added to url patterns like how
# you add your views

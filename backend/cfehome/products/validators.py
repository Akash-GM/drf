from rest_framework import serializers
from .models import Product
from rest_framework.validators import UniqueValidator


# def validate_title(value):
#     qs = Product.objects.filter(title__exact=value)
#     if qs.exists():
#         raise serializers.ValidationError(f"{value} already exists")
#     return value


def validate_title_no_hello(value):
    if "hello" in value:
        raise serializers.ValidationError("Cannot contain hello")
    return value


unique_product_title = UniqueValidator(
    queryset=Product.objects.all(), message="This title is already in use."
)

from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name="product-detail", lookup_field="pk"
    )
    email = serializers.EmailField(write_only=True)
    # update_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = [
            "url",
            # "update_url",
            "email",
            "title",
            "content",
            "price",
            "sale_price",
            "my_discount",
        ]

    # def create(self, validated_data):
    #     # email = validated_data.pop("email")
    #     validated_data["price"] = 0
    #     obj = super().create(validated_data)
    #     # obj.email = email
    #     print(obj.__dict__)
    #     return obj

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get("title", instance.title)
    #     return instance

    """def get_url(self, obj):
        # return f"/api/products/{obj.pk}/"
        request = self.context.get("request")

        if request is None:
            return None

        return reverse("product-detail", kwargs={"pk": obj.pk}, request=request)"""

    def get_update_url(self, obj):
        # return f"/api/products/{obj.pk}/"
        request = self.context.get("request")

        if request is None:
            return None

        return reverse("product-update", kwargs={"pk": obj.pk}, request=request)

    def get_my_discount(self, obj):
        if not hasattr(obj, "id"):
            return None
        if not isinstance(obj, Product):
            return None

        return obj.get_discount()

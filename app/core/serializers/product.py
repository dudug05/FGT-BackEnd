from rest_framework.serializers import ModelSerializer

from core.models import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


def create(self, validated_data):
    itens = validated_data.pop("itens")
    product = Product.objects.create(**validated_data)
    for item in itens:
        item["price"] = item["product"].price # nova linha
        Product.objects.create(product=product, **item)
    product.save()
    return product
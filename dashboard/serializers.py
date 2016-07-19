from rest_framework import serializers


from models import Category, Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    product = ProductSerializer

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'product', 'parent_category']

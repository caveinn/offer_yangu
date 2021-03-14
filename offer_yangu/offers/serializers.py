from .models import Offers, Category, Location
from rest_framework import serializers


class CategoryField(serializers.Field):
    def to_representation(self, value):
        return value.name

    def to_internal_value(self, data):
        return Category.objects.get(id=int(data))


class LocationField(serializers.Field):
    def to_representation(self, value):
        return value.name

    def to_internal_value(self, data):
        return Location.objects.get(id=int(data))


class OffersSerializer(serializers.ModelSerializer):
    seller = serializers.SerializerMethodField(required=False)
    category = CategoryField()
    location = CategoryField()

    class Meta:
        model = Offers
        fields = "__all__"

    def create(self, validated_data):
        validated_data["seller"] = self.context.get("request").user
        return super().create(validated_data)

    def get_seller(self, obj):
        return {
            "username": obj.seller.username,
            "email": obj.seller.email
        }


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class LocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"

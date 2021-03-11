from .models import Offers, Category
from rest_framework import serializers
from offer_yangu.authentication.models import User


class CategoryField(serializers.Field):
    def to_representation(self, value):
        return value.name
    def to_internal_value(self, data):
        return Category.objects.get(id=int(data))



class OffersSerializer(serializers.ModelSerializer):
    seller = serializers.SerializerMethodField(required=False)
    category = CategoryField()
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

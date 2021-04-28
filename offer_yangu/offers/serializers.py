from .models import Offers, Category, Location, OfferReview
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class CategoryField(serializers.Field):
    def to_representation(self, value):
        return value.name

    def to_internal_value(self, data):
        try:
            return Category.objects.get(id=int(data))
        except:
            raise ValidationError("category is required")


class LocationField(serializers.Field):
    def to_representation(self, value):
        return value.name

    def to_internal_value(self, data):
        try:
            return Location.objects.get(id=int(data))
        except:
            raise ValidationError("Location is required")

class ReviewSerializer(serializers.ModelSerializer):
    reviewer = serializers.SerializerMethodField(required=False)
    class Meta:
        model = OfferReview
        fields = "__all__"

    # def create(self, validated_data):
    #     validated_data["reviewer"] = self.context.get("request").user
    #     return super().create(validated_data)

    def get_reviewer(self, obj):
        return {
            "username": obj.reviewer.username,
            "email": obj.reviewer.email,
            "phone": obj.reviewer.phone_number,
            "joined": obj.reviewer.created_at,
        }
class OffersSerializer(serializers.ModelSerializer):
    seller = serializers.SerializerMethodField(required=False)
    category = CategoryField()
    location = LocationField()

    class Meta:
        model = Offers
        fields = "__all__"

    def create(self, validated_data):
        validated_data["seller"] = self.context.get("request").user
        return super().create(validated_data)

    def get_seller(self, obj):
        return {
            "username": obj.seller.username,
            "email": obj.seller.email,
            "phone": obj.seller.phone_number,
            "joined": obj.seller.created_at,
        }


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class LocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"

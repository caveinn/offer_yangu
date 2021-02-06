from .models import Offers
from rest_framework import serializers
from offer_yangu.authentication.models import User


class OffersSerializer(serializers.ModelSerializer):
    seller = serializers.SerializerMethodField(required=False)
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

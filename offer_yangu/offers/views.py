from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from ..helpers.pagination_helper import Pagination
from .models import Category, Offers, Location
from .serializers import CategoriesSerializer, OffersSerializer, LocationsSerializer

from rest_framework.decorators import action


class OffersViewset(ModelViewSet):
    serializer_class = OffersSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    parser_classes = (MultiPartParser, FormParser)
    pagination_class = Pagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['name_of_product', "location", "category", "top_offer"]
    search_fields = ['name_of_product', "description", ]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Offers.objects.all()
        return Offers.objects.filter(approved=True)

    @action(methods=['GET'], detail=False, url_name='Search offers')
    def get(self, request, *args, **kwargs):
        """
        Search Ofers
        """
        return super().list(request, *args, **kwargs)


class CategoriesViewset(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]


class LocationsViewset(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]

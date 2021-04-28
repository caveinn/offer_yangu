from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from rest_framework import status, views, generics

from ..helpers.pagination_helper import Pagination
from .models import Category, Offers, Location, OfferReview
from .serializers import CategoriesSerializer, OffersSerializer, LocationsSerializer, ReviewSerializer

from rest_framework.decorators import action
from rest_framework.response import Response


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


class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = OfferReview.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def post(self, request, id):
        """
        Method for creating review
        """

        offer = None
        try:
            offer = Offers.objects.get(id=id)
        except:
            return Response(
                status=404,
                data={
                    'message': 'offer with that id does not exist'
                }
            )
        review = request.data
        review['reviewer'] = request.user.id
        review['offer'] = offer.pk
        serializer = self.serializer_class(data=review)
        serializer.is_valid(raise_exception=True)
        serializer.save(reviewer = request.user)
        # serializer.save(author=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, id):
        """
        Method for getting all comments
        """

        offer = None
        try:
            offer = Offers.objects.get(id=id)
        except:
            return Response(
                status=404,
                data={
                    'message': 'offer with that id does not exist'
                }
            )
        reviews = offer.reviews.filter()
        serializer = self.serializer_class(
            reviews.all(), context={'request': request}, many=True)
        data = {
            'count': reviews.count(),
            'reviews': serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)

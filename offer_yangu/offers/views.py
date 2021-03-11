from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework.permissions import AllowAny,IsAuthenticatedOrReadOnly
from rest_framework.parsers import FormParser, MultiPartParser


# Create your views here.


class OffersViewset(ModelViewSet):
    serializer_class = OffersSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]
    parser_classes = (MultiPartParser,FormParser)

    def get_queryset(self):
        if self.request.user.is_staff:
            return Offers.objects.all()
        return Offers.objects.filter(approved=True)


class CategoriesViewset(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]

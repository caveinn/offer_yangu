from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework.permissions import AllowAny,IsAuthenticatedOrReadOnly


# Create your views here.


class OffersViewset(ModelViewSet):
    queryset = Offers.objects.all()
    serializer_class = OffersSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


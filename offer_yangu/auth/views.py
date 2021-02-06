from django.shortcuts import render
import jwt
from rest_framework.permissions import AllowAny
from .serializers import RegistrationSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status

class RegistrationAPIView(CreateAPIView):
    # Allow any user (authenticated or not) to hit this endpoint.
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {} )

        # The create serializer, validate serializer, save serializer pattern
        # below is common and you will see it a lot throughout this course and
        # your own work later on. Get familiar with it.
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response("User created successfully", status=status.HTTP_201_CREATED)

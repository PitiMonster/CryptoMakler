import json
import time

import requests
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny

from .serializers import RegisterSerializer, UserProfileSerializer


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            user_data = {
                "email": request.POST.get('email'),
                "username": request.POST.get('username'),
                "password": request.POST.get('password'),
            }

            duplicate_users = User.objects.filter(email=user_data.get("email"))
            if not len(duplicate_users) == 0:
                raise Exception('This email is already registered')

            user_serializer = RegisterSerializer(data=user_data)
            if not user_serializer.is_valid():
                raise Exception('Problem with data validation')

            user = user_serializer.save()

            role_data = {
                'user': user.pk,
                'role': request.POST.get('role')
            }
            role_serializer = UserProfileSerializer(data=role_data)

            if not role_serializer.is_valid():
                user.delete()
                raise Exception('Problem with role selection')

            role_serializer.save()
            return Response("User Created Successfully. Now login to get your token", status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({str(e)}, status=status.HTTP_406_NOT_ACCEPTABLE)


class TestTokenView(APIView):
    def get(self, request):
        return Response("Token is valid", status=status.HTTP_200_OK)

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from authentication.views import AuthenticationView
from .serializers import UserSerializer

class UserAPIView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():

            user = serializer.save()

            refreshToken = AuthenticationView().get_tokens(user)

            return Response({
                'refresh': str(refreshToken),
                'access': str(refreshToken.access_token),
            }, status=status.HTTP_201_CREATED)


from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from authentication.views import AuthenticationView
from .serializers import UserSerializer
import bcrypt

class UserAPIView(APIView):

    def post(self, request):

        salt = bcrypt.gensalt()
        request.data['password'] = bcrypt.hashpw(request.data['password'].encode('utf-8'), salt).decode('utf-8')

        print(request.data)

        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():

            user = serializer.save()

            token = AuthenticationView().get_tokens(user)

            return Response({
                'token': str(token),
                'user': serializer.data,
            }, status=status.HTTP_201_CREATED)


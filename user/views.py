from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from authentication.views import AuthenticationView
from .serializers import UserSerializer
import bcrypt
from .models import User

class RegistrationUserAPIView(APIView):

    def post(self, request):

        salt = bcrypt.gensalt()
        request.data['password'] = bcrypt.hashpw(request.data['password'].encode('utf-8'), salt).decode('utf-8')

        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():

            user = serializer.save()

            token = AuthenticationView().get_token(user)

            return Response({
                'token': str(token),
                'user': serializer.data,
            }, status=status.HTTP_201_CREATED)
        
class LoginUserAPIView(APIView):

    def post(self, request):


        data = request.data
        user = User.objects.get(username=data['username'])
        serializer = UserSerializer(user).data

        if bcrypt.checkpw(data['password'].encode('utf-8'), serializer['password'].encode('utf-8')):
            token = AuthenticationView().get_token(user)

            return Response({
                'token': token,
                'user': serializer
            }, status=status.HTTP_200_OK)
       





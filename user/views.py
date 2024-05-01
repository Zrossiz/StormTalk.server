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
        try:
            data = request.data
            if 'password' not in data:
                return Response({
                    'success': False,
                    'message': 'password not found'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            if 'username' not in data:
                return Response({
                    'success': False,
                    'message': 'username not found'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            if 'email' not in data:
                return Response({
                    'success': False,
                    'message': 'email not found'
                }, status=status.HTTP_400_BAD_REQUEST)
            

            salt = bcrypt.gensalt()
            data['password'] = bcrypt.hashpw(data['password'].encode('utf-8'), salt).decode('utf-8')

            serializer = UserSerializer(data=data)

            if serializer.is_valid():

                user = serializer.save()

                token = AuthenticationView().get_token(user)

                return Response({
                    'token': str(token),
                    'user': serializer.data,
                }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({
                'success': False,
                'message': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        
class LoginUserAPIView(APIView):

    def post(self, request):
        try:
            data = request.data

            if 'password' not in data:
                return Response({
                    'success': False,
                    'message': 'password not found'
                }, status=status.HTTP_400_BAD_REQUEST)
            
        
            if 'username' not in data:
                return Response({
                    'success': False,
                    'message': 'username not found'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            user = User.objects.get(username=data['username'])

            serializer = UserSerializer(user).data

            if bcrypt.checkpw(data['password'].encode('utf-8'), serializer['password'].encode('utf-8')):
                token = AuthenticationView().get_token(user)

                return Response({
                    'success': True,
                    'token': token,
                    'user': serializer
                }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'success': False,
                'message': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
       





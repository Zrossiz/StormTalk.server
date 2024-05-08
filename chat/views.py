from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from authentication.views import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from chat.models import Chat
from chat.serializers import ChatSerializer
from user.models import User

class CreateChatAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            data = request.data
            first_user = User.objects.get(pk=int(data['user'].id))
            second_user = User.objects.get(pk=int(data['to_user']))
            
            new_chat = Chat.objects.create(first_user=first_user, second_user=second_user)

            serializer = ChatSerializer(new_chat).data

            return Response({
                'success': True,
                'data': serializer
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({
                'success': False,
                'message': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UpdateChatAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, chat_id):
        try:
            try:
                chat = Chat.objects.get(pk=chat_id)
            except Exception as e:
                return Response({
                    'success': False,
                    'data': 'not found'
                }, status=status.HTTP_404_NOT_FOUND)
            serializer = ChatSerializer(chat).data
            if serializer:
                chat.delete()
                return Response({
                    'success': True,
                    'data': serializer
                }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                'success': False,
                'message': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
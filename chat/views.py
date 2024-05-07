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

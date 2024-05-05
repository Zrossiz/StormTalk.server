from rest_framework.views import APIView
from .serializers import SubscribeSerializer
from authentication.views import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from user.models import User
from .models import Subscribe


class CreateSubcsribeAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            data = request.data
            user_author_id = int(data['author']['id'])

            try:
                User.objects.get(pk=user_author_id)
            except Exception as e:
                return Response({
                    'success': False,
                    'message': 'author not found'
                }, status=status.HTTP_404_NOT_FOUND)

            create_subscribe_data ={
                'listener': data['user'].id,
                'author': user_author_id
            }

            serializer = SubscribeSerializer(data=create_subscribe_data)

            if serializer.is_valid():
                serializer.save()
                return Response({
                    'success': True,
                    'data': serializer.data
                }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({
                'success': False,
                'message': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UpdateSubscribeAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, post_id):
        try:
            data = request.data
            user_id = int(data['user'].id)
            
            subscribe = Subscribe.objects.get(pk=post_id)
            serializer = SubscribeSerializer(subscribe).data
            if serializer['listener'] == user_id:
                subscribe.delete()
                return Response({
                    'success': True,
                    'data': serializer
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'success': False,
                    'message': 'Forbidden'
                }, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({
                'success': False,
                'message': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


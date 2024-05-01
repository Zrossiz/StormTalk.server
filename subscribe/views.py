from rest_framework.views import APIView
from .serializers import SubscribeSerializer
from authentication.views import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


class CreateSubcsribeAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            data = request.data

            create_subscribe_data ={
                'listener': data['user'].id,
                'author': int(data['author']['id'])
            }

            serializer = SubscribeSerializer(data=create_subscribe_data)

            if serializer.is_valid():
                serializer.save()
                return Response({
                    'success': True,
                    'data': serializer.data
                })
        except Exception as e:
            return Response({
                'success': False,
                'message': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

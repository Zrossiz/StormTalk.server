from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from authentication.views import JWTAuthentication
from .serializers import PostSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class PostAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="Create post",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "post": openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "description": openapi.Schema(type=openapi.TYPE_STRING),
                        "image": openapi.Schema(type=openapi.TYPE_STRING)
                    }
                )
            },
            required=["post"]
        ),
        responses={200: "Success response description"},
        security=[{"Bearer": []}]  # Указываем, что эндпоинт требует аутентификации
    )
    def post(self, request):
        data = request.data

        try:
            if 'description' not in data['post']:
                return Response({
                    'success': False,
                    'message': 'description not found'
                }, status=status.HTTP_400_BAD_REQUEST)
                                    
            create_post_data = {
                'user': data['user'].id,
                'description': data['post']['description'],
                'image': data['post']['image'] if 'image' in data['post'] else None
            }

            serializer = PostSerializer(data=create_post_data)

            if serializer.is_valid():
                serializer.save()
                return Response({
                    'success': True,
                    'data': serializer.data
                })
            else:
                raise Exception('create post error')
        except Exception as e:
            return Response({
                'success': False,
                'message': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
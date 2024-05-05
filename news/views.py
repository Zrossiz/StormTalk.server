from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from authentication.views import JWTAuthentication
from post.models import Post
from post.serializers import PostSerializer
from subscribe.models import Subscribe
from subscribe.serializers import SubscribeSerializer


class NewsAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            data = request.data

            user_id = int(data['user'].id)

            all_authors_by_user = Subscribe.objects.filter(listener=user_id)
            authors_serializer = SubscribeSerializer(all_authors_by_user, many=True).data
            author_ids_arr = []

            for author_data in authors_serializer:
                author_ids_arr.append(author_data["author"])

            all_posts_by_authors = Post.objects.filter(user__in=author_ids_arr).order_by('created_at')
            posts_serializer = PostSerializer(all_posts_by_authors, many=True).data

            if len(posts_serializer) == 0:
                return Response({
                    'success': True,
                    'data': 'not found'
                }, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({
                    'success': True,
                    'data': posts_serializer
                }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'success': False,
                'message': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
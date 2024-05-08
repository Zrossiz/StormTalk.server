import jwt
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from core.settings import SECRET_KEY
from user.models import User
import datetime


class AuthenticationView:

    def get_token(self, user):
        payload = {
            'id': user.id,
            'name': user.username,
            'email': user.email,
            'exp': datetime.datetime.now() + datetime.timedelta(days=1)
        }

        token = jwt.encode(payload, SECRET_KEY, 'HS256')

        return token
    

class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.headers.get('Authorization')

        if not token:
            return None

        try:
            payload = jwt.decode(str(token).split(' ')[1], SECRET_KEY, algorithms=['HS256'])
            user_id = payload['id']
            user = User.objects.get(pk=user_id)
            request.data['user'] = user
            return (user, None)
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token expired')
        except jwt.InvalidTokenError:
            raise AuthenticationFailed('Invalid token')
        except User.DoesNotExist:
            raise AuthenticationFailed('User not found')

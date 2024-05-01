from StormTalk.settings import SECRET_KEY
import jwt
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
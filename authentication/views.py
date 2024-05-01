from StormTalk.settings import SECRET_KEY
import jwt

class AuthenticationView:

    def get_tokens(self, user):
        payload = {
            'id': user.id,
            'name': user.username,
            'email': user.email
        }

        token = jwt.encode(payload, SECRET_KEY, 'HS256')

        return token
from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
class AuthenticationView:

    def get_tokens(self, user):
        refresh = RefreshToken.for_user(user) # Создание Refesh и Access

        refresh.payload.update({    # Полезная информация в самом токене
            'user_id': user.id,
            'username': user.username
        })

        return refresh
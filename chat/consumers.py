from channels.generic.websocket import AsyncWebsocketConsumer
import json
from rest_framework.permissions import IsAuthenticated
from authentication.views import JWTAuthentication
from .models import Chat


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self, request):
        self.chat_id = self.scope['url_route']['kwargs']['chat_id']
        self.room_group_name = 'chat_%s' % self.chat_id

        # chat = Chat.objects.get_or_create(
        #     pk=self.chat_id,
        #     defaults={'first_user_id': first_user_id, 'second_user_id': second_user_id}
        # )

        chat = True

        if chat:
            # Join room group
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )

            await self.accept()
        else:
            self.close()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))

from channels.generic.websocket import AsyncWebsocketConsumer
import json
from message.models import Message
from asgiref.sync import sync_to_async



class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = "chat_%s" % self.scope["url_route"]["kwargs"]["chat_id"]
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        print("Receive: ", text_data)
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        await sync_to_async(Message.objects.create)(text=message, 
                               sender_id=text_data_json["sender"],
                               chat_id=text_data_json["chat"]
                            )
        if message:
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "chat_message",
                    "data": text_data_json
                }
            )

    async def chat_message(self, event):
        print("Message: ", event)
        message = event["data"]["message"]
        await self.send(text_data=json.dumps({
            "message": message
        }))

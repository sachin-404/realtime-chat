import json
import django
django.setup()

# from django.contrib.auth.models import User
from channels.generic.websocket import AsyncWebsocketConsumer
# from asgiref.sync import sync_to_async
from channels.db  import database_sync_to_async

from django.contrib.auth import get_user_model
User = get_user_model()

from nltk.tag import pos_tag
from nltk.tokenize import RegexpTokenizer

from .models import Room, Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        
    #receive message from WebSocket
    async def receive(self, text_data):
        data = json.loads(text_data)
        print(data)
        message = data['message']
        username = data['username']
        room = data['room']
        
        tokenizer = RegexpTokenizer(r'\w+')
        tagged = pos_tag(tokenizer.tokenize(message))
        #figure of speech
        fos = '{' + ', '.join([f'{word}: {pos}' for word, pos in tagged]) + '}'

        await self.save_message(username, room, message, fos)

        #send recieved message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'fos': fos,
                'username': username,
                'room': room
            }
        )

    #receive message from room group
    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        room = event['room']
        fos = event['fos']

        #send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'fos': fos,
            'username': username,
            'room': room
        }))
    
    @database_sync_to_async
    def save_message(self, username, room, message, fos):
        user = User.objects.get(username=username)
        room = Room.objects.get(slug=room)
        
        Message.objects.create(user=user, room=room, content=message, fos=fos)
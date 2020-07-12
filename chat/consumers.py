from channels.generic.websocket import AsyncWebsocketConsumer
import chat, user
from django.utils import timezone
import datetime
from django.forms.models import model_to_dict
import json

class DateTimeEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, datetime.datetime):
            return (str(z))
        else:
            return super().default(z)

class Chatter(AsyncWebsocketConsumer):
    async def connect(self):
        #self.service_uid = self.scope["url_route"]["kwargs"]["service_uid"]
        self.chat_group_name = 'nonechat'
        # self.channel_name = 'all-channel'
        # 收到连接时候处理，
        await self.channel_layer.group_add(
            self.chat_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # 关闭channel时候处理
        await self.channel_layer.group_discard(
            self.chat_group_name,
            self.channel_name
        )

    # 收到消息
    async def receive(self, text_data):
        message = text_data
        print("{}: {}".format(self.scope['session']['username'], message))
        content = message
        sender = user.models.User.objects.get(username=self.scope['session']['username'])
        msg = chat.models.Message.objects.create(sender=sender, content=content, time=timezone.now())
        if msg:
            data = json.dumps(model_to_dict(msg), cls=DateTimeEncoder)
            data = json.loads(data)
            data['sender'] = self.scope['session']['rand_name']
            data['style'] = self.scope['session']['rand_style']
            data = json.dumps(data)
            # 发送消息到组
            await self.channel_layer.group_send(
                self.chat_group_name,
                {
                    'type': 'client.message',
                    'message': data
                }
            )
        else:
            pass

    # 处理客户端发来的消息
    async def client_message(self, event):
            # 发送消息到 WebSocket
            await self.send(text_data=event['message'])
        
from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    url(r'chat/send/', consumers.Chatter), #该路由的消费者
]
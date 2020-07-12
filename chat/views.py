from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# #from dwebsocket.decorators import accept_websocket,require_websocket
# from channels.layers import get_channel_layer
# from asgiref.sync import async_to_sync
# import chat, user
# from django.utils import timezone
# import datetime
# from django.forms.models import model_to_dict
# import json

# class ChatRoom():
#     connections = []

# class DateTimeEncoder(json.JSONEncoder):
#     def default(self, z):
#         if isinstance(z, datetime.datetime):
#             return (str(z))
#         else:
#             return super().default(z)

# channel_layer = get_channel_layer()

# Create your views here.
# @accept_websocket
def send(request):
    # if not request.is_websocket():#判断是不是websocket连接age)
    #     return JsonResponse({'error': '不安全的访问方式，服务器已拒绝。'})
    # else:
    #     if request.websocket not in ChatRoom.connections:
    #         ChatRoom.connections.append(request.websocket)
    #     # 遍历请求地址中的消息
    #     for message in request.websocket:
    #         # 消息保存至数据库(为了方便查看聊天记录)
    #         # print(str(message, encoding="utf-8"))
    #         if message == None:
    #             continue
    #         content = str(message, encoding="utf-8")
    #         sender = user.models.User.objects.get(username=request.session['username'])
    #         msg = chat.models.Message.objects.create(sender=sender, content=content, time=timezone.now())
    #         if msg:
    #             # 将信息发至其他所有用户的聊天框
    #             # for connection in ChatRoom.connections:
    #             #     if not connection.is_closed():
    #             #         data = json.dumps(model_to_dict(msg), cls=DateTimeEncoder)
    #             #         data = json.loads(data)
    #             #         data['sender'] = request.session['rand_name']
    #             #         data['style'] = request.session['rand_style']
    #             #         data = json.dumps(data)
    #             #         connection.send(data)
    #             #     else:
    #             #         ChatRoom.connections.remove(connection)
    #             data = json.dumps(model_to_dict(msg), cls=DateTimeEncoder)
    #             data = json.loads(data)
    #             data['sender'] = request.session['rand_name']
    #             data['style'] = request.session['rand_style']
    #             data = json.dumps(data)
    #             data['type'] = "client message"
    #             async_to_sync(channel_layer.group_send)("nonechat", data)
    #         else:
    #            pass
    pass



from django.urls import path, re_path, include
from chat import views

urlpatterns = [
    path(r'send/', views.send, name="发送消息"), # 仅仅做名称解析，实际跳转其实失效
]
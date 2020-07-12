from django.urls import path, re_path, include
from user import views

urlpatterns = [
    path(r'login/', views.login, name="用户登录"),
    path(r'logout/', views.logout, name="用户登出"),
]

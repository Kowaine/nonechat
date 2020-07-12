from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from user import models
from django.utils import timezone
import re
from user.tools import add_format_info
from django.utils.safestring import mark_safe



username_re = re.compile(r"^[0-9a-zA-Z_]{3,14}$")
password_re = re.compile(r"^[0-9a-zA-Z_#*&]{8,14}$")

# Create your views here.
def is_exist(username):
    if models.User.objects.filter(username=username).exists():
        return True
    else:
        return False

def vaildate_user(username, password):
    if models.User.objects.filter(username=username, password=password).exists():
        return True
    else:
        return False

def create_user(username, password, ip, time):
    user = models.User.objects.create(username=username, password=password, last_ip=ip, register_time=time)
    if user:
        return True
    else:
        return False

def check_format(username, password):
    error_msg = ""
    flag = True
    if username_re.match(username) == None:
        error_msg += "用户名仅能包含字母、数字或下划线，长度在[3, 14]之间<br/>"
        flag = False
    if password_re.match(password) == None:
        error_msg += "密码仅能包含字母、数字、下划线或#、*、&，长度在[8, 14]之间<br/>"
        flag = False

    return flag, mark_safe(error_msg)

    


def login(request):
    if request.method=="GET":
        return HttpResponse("{'msg':'不安全的请求，服务器已拒绝'}")

    username = request.POST['username']
    password = request.POST['password']

    is_ok, msg = check_format(username, password)
    if not is_ok:
        data = {}
        data['error_msg'] = msg
        data['old_username'] = username
        data = add_format_info(data)
        return render(request, 'login.html', data)

    if is_exist(username):
            if vaildate_user(username, password):
                request.session['is_login'] = True
                request.session['username'] = username
                models.User.objects.filter(username=username).update(last_ip=request.META['REMOTE_ADDR'])
                return redirect("/")
            else:
                # 携带错误信息返回
                data = {}
                data['error_msg'] = "密码错误"
                data['old_username'] = username
                data = add_format_info(data)
                return render(request, 'login.html', data)
                
    else:
        create_user(username, password, request.META['REMOTE_ADDR'], timezone.now())
        request.session['is_login'] = True
        request.session['username'] = username
        return redirect("/")

def logout(request):
    request.session.clear()
    data = {}
    data = add_format_info(data)
    return render(request, 'login.html', data)
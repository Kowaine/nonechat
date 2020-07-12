from django.http import HttpResponse
from django.shortcuts import render
import random
from user.tools import add_format_info

rand_length = 8
style_list = ["aquamarine", "cornflowerblue", "brown", "blueviolet", "dodgerblue", "forestgreen", "hotpink", "gold"]

def randstr(num):
    H = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

    salt = ''
    for i in range(num):
        salt += random.choice(H)

    return salt
 
def hello(request):
    return HttpResponse("Hello world ! ")

def index(request):
    data = {}
    if 'is_login' in request.session and request.session['is_login']:
        data['hello'] = "Hello " + request.session['username']
        if 'rand_name' not in request.session:
            data['rand_name'] = randstr(rand_length)
            request.session['rand_name'] = data['rand_name']
        else:
            data['rand_name'] = request.session['rand_name']
        if 'rand_style' not in request.session:
            data['rand_style'] = random.choice(style_list)
            request.session['rand_style'] = data['rand_style']
        else:
            data['rand_style'] = request.session['rand_style']

        return render(request, "index.html", data)
    else:
        data = add_format_info(data)
        return render(request, "login.html", data)


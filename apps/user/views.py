from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
# from django.core.urlresolvers import  resolve
from django.conf import settings
from django.urls import reverse
from django.shortcuts import render, redirect
from itsdangerous import  TimedJSONWebSignatureSerializer as Serializer

import re
from apps.user.models import User


# Create your views here.


def index(request):
    str = '3.3333'
    return HttpResponse(str)


def register(request):
    # str = 'jjjjj'
    # return HttpResponse(str)
    return render(request, 'register.html')


def register_handle(request):
    '''注册处理'''
    # 接受数据

    username = request.POST.get('user_name')
    password = request.POST.get('pwd')
    email = request.POST.get('email')
    allow = request.POST.get('allow')
    print(username + '--' + password + '----' + email)

    # 校验数据
    if not all([username, password, email]):
        # 数据不完整
        content = {'errmsg': '数据不完整'}
        return render(request, 'register.html', content)
    if not re.match(r'^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
        content = {'errmsg': '邮箱不合法'}
        return render(request, 'register.html', content)
    if allow != 'on':
        content = {'errmsg': '同意协议'}
        return render(request, 'register.html', content)

    # 业务处理
    # user = User()
    # user.username=username
    user = User.objects.create_user(username, email, password)
    user.is_active = 0
    user.save()
    # 返回数据
    # return redirect(reverse('goods:index'))
    return render(request, 'index.html')


class RegisterView(View):

    def get(sele, request):
        return render(request, 'register.html')

    def post(sele, request):
        username = request.POST.get('user_name')
        password = request.POST.get('pwd')
        email = request.POST.get('email')
        allow = request.POST.get('allow')
        print(username + '--' + password + '----' + email)

        # 校验数据
        if not all([username, password, email]):
            # 数据不完整
            content = {'errmsg': '数据不完整'}
            return render(request, 'register.html', content)
        if not re.match(r'^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            content = {'errmsg': '邮箱不合法'}
            return render(request, 'register.html', content)
        if allow != 'on':
            content = {'errmsg': '同意协议'}
            return render(request, 'register.html', content)

        # 业务处理
        # user = User()
        # user.username=username
        user = User.objects.create_user(username, email, password)
        user.is_active = 0
        user.save()

        #  发送邮件 包含激活链接
        # 加密用户的身份信息  生成激活token
        serializer = Serializer(settings.SECRET_KEY,3600)
        info = {'confirm':user.id}
        token = serializer.dumps(info)
        # 链接包含用户信息
        #
        # 返回数据
        # return redirect(reverse('goods:index'))
        return render(request, 'index.html')

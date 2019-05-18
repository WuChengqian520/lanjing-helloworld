# -*- coding: utf-8 -*-
from django.shortcuts import render
from blueapps.account.decorators import login_exempt
from django.http import JsonResponse

# 开发框架中通过中间件默认是需要登录态的，如有不需要登录的，可添加装饰器login_exempt
# 装饰器引入 from blueapps.account.decorators import login_exempt

@login_exempt
def home(request):
    """
    首页
    """
    return render(request, 'home_application/helloworld.html')


@login_exempt
def second(request):
    """
    第二次作业：判断，返回
    """
    if request.method == "GET":
        return render(request, 'home_application/inpnut_output.html')
    elif request.method == "POST":
        input_value = request.POST.get('input2').strip()
        if input_value == "Hello Blueking":
            return JsonResponse({'code': 200})
        else:
            return JsonResponse({"code": 400})

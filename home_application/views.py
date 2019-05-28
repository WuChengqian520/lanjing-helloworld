# -*- coding: utf-8 -*-
from django.shortcuts import render
from blueapps.account.decorators import login_exempt
from django.http import JsonResponse
from .models import Mainframe

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


@login_exempt
def third(request):
    if request.method == "GET":
        return render(request, 'home_application/record.html')
    elif request.method == "POST":
        name = request.POST.get('name')
        ip = request.POST.get('ip')
        subarea = request.POST.get('subarea')
        system = request.POST.get('system')
        remark = request.POST.get('remark')
        Mainframe.objects.create(
            name=name,
            ip=ip,
            subarea=subarea,
            system=system,
            remark=remark
        )
        return JsonResponse({"code": 200})


data = {
    "catalogues": {
        "index": "#",
        "name": "主机名",
        "ip": "IP地址",
        "subarea": "常用分区",
        "system": "操作系统",
        "remark": "备注",
        "create_time": "录入时间"
    },
    "items": [],
    "code": 200
}


@login_exempt
def get_mainframe(request):
    mainframes = Mainframe.objects.all()
    data['items'] = []
    for i in mainframes:
        data['items'].append({
            "index": i.id,
            "name": i.name,
            "ip": i.ip,
            "subarea": i.subarea,
            "system": i.system,
            "remark": i.remark,
            "create_time": i.create_time
        })
    return JsonResponse(data)


@login_exempt
def search_host(request):
    ip = request.GET.get('ip')
    mainframe = Mainframe.objects.filter(ip=ip)
    if not mainframe:
        return JsonResponse({'code': 400})
    mainframe = mainframe.first()
    data['items'] = []
    data['items'].append({
        "index": mainframe.id,
        "name": mainframe.name,
        "ip": mainframe.ip,
        "subarea": mainframe.subarea,
        "system": mainframe.system,
        "remark": mainframe.remark,
        "create_time": mainframe.create_time
    })
    return JsonResponse(data)

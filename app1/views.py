
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render  # 引入Django提供的渲染页面函数render，将网页内容转换成符合http传输的二进制文件
# 创建app1函数与request参数
from app1.qt.method import qt, cat


def app1(request):
    return render(request,'helloWorld.html')


def hello(request):
    color = request.GET.get("color")
    age = request.GET.get("age")
    c = cat(age,color)

    return render(request,'helloWorld.html',context ={'cat':c} )

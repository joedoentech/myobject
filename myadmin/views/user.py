# 员工信息管理视图文件
from hashlib import md5
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from myadmin.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from datetime import datetime

# Create your views here.


def index(request, pindex=1):
    # 浏览信息
    umod = User.objects
    ulist = umod.filter(status__lt=9)
# 获取查询
    kw = request.GET.get("keyword", None)
    if kw:
        ulist = ulist.filter(Q(username__contains=kw) | Q(nickname__contains=kw))
# 执行分页
    pindex = int(pindex)
    page = Paginator(ulist, 5)
    maxpage = page.num_pages
    if pindex > maxpage:
        pindex = maxpage
    if pindex < 1:
        pindex = 1
    list2 = page.page(pindex)
    plist = page.page_range

    context = {"userlist": list2, 'plist': plist,
               'pindex': pindex, 'maxpages': maxpage}
    return render(request, 'myadmin/user/index.html', context)
    mywhere.append("keyword="+kw)


def add(request):
    # 加载信息添加表单
    return render(request, 'myadmin/user/add.html')


def insert(request):
    # 执行信息添加
    try:
        ob = User()
        ob.username = request.POST['username']
        ob.nickname = request.POST['nickname']

        import hashlib
        import random
        md5 = hashlib.md5()
        n = random.randint(100000, 999999)
        s = request.POST['password']+str(n)
        md5.update(s.encode('utf-8'))
        ob.password_hash = md5.hexdigest()
        ob.password_salt = n

        ob.status = 1
        ob.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': "添加成功"}

    except Exception as err:
        print(err)
        context = {'info': "添加失败"}
    return render(request, "myadmin/info.html", context)


def delete(request,uid=0):
    # 执行信息删除
    try:
        ob = User.objects.get(id=uid)
        ob.status = 9
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': "删除成功"}
    except Exception as err:
        print(err)
        context = {'info': "删除失败"}
    return render(request,'myadmin/info.html',context)


def edit(request, uid=0):
    # 加载信息编辑
    try:
        ob = User.objects.get(id=uid)
        context = {'user': ob}
        return render(request,'myadmin/user/edit.html',context)
    except Exception as err:
        print(err)
        context = {'info': "没有找到要修改的信息"}
        return render(request,'myadmin/info.html',context)
    
# 浏览信息


def update(request, uid=0):
    # 执行信息编辑
    try:
        ob = User.objects.get(id=uid)
        ob.nickname = request.POST['nickname']
        ob.status = request.POST['status']
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': "修改成功"}
    except Exception as err:
        print(err)
        context = {'info': "修改失败"}
    return render(request,'myadmin/info.html',context)


def edit(request, uid=0):
    # 加载信息编辑
    try:
        ob = User.objects.get(id=uid)
        ob.nickname = request.POST['nickname']
        ob.status = request.POST['status']
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': "修改成功"}
        return render(request,'myadmin/user/edit.html',context)
    except Exception as err:
        print(err)
        context = {'info': "修改失败"}
        return render(request,'myadmin/info.html',context)

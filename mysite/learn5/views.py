# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .forms import AddForm

from learn5.models import Member,Material,Running,Running_Member,Running_Material


import time


if (0==len(Member.objects.filter(name='namea'))):
    Member.objects.create(name='namea', funds=0)
if (0==len(Member.objects.filter(name='nameb'))):
    Member.objects.create(name='nameb', funds=0)
if (0==len(Member.objects.filter(name='namec'))):
    Member.objects.create(name='namec', funds=0)


def index(request):
    if request.method == 'POST':# 当提交表单时
        form = AddForm(request.POST) # form 包含提交的数据
        if form.is_valid():# 如果提交的数据合法
            ra=Running.objects.create(itemname =form.cleaned_data['r'],itemtime=time.time())
            ma=Material.objects.create(name='Materiala', number=form.cleaned_data['a'],units='个',total=0,remark='无')
            mb=Material.objects.create(name='Materialb', number=form.cleaned_data['b'],units='个',total=0,remark='无')
            mc=Material.objects.create(name='Materialc', number=form.cleaned_data['c'],units='个',total=0,remark='无')
            rtm=Running_Material.objects.create()
            rtm.runnings.add(ra)
            rtm.materials.add(ma)
            rtm.materials.add(mb)
            rtm.materials.add(mc)

    # else:# 当正常访问时
    form = AddForm()
    d=Material.objects.all()
    dlist1=[]
    # dlist1.append("<th>id</th> <th>name</th> <th>number</th> <th>units</th> <th>total</th> <th>remark</th>")
    i=0
    for a in d:
        dlist1.append([])
        dlist1[i].append(a.id)
        dlist1[i].append(a.name)
        dlist1[i].append(a.number)
        dlist1[i].append(a.units)
        dlist1[i].append(a.total)
        dlist1[i].append(a.remark)
        
        i=i+1

    d=Member.objects.all()
    dlist2=[]
    # dlist2.append("<th>id</th> <th>name</th> <th>funds</th> <th>remark</th>")
    i=0
    for a in d:
        dlist2.append([])
        dlist2[i].append(a.id)
        dlist2[i].append(a.name)
        dlist2[i].append(a.funds)
        dlist2[i].append(a.remark)
        
        i=i+1
    return render(request,'index.html', {'form': form,'dlist1': dlist1,'dlist2': dlist2})


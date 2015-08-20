# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .forms import AddForm

from learn5.models import Member,Material,Running,Running_Member,Running_Material


import time


# Material_tmp=[['Materiala'],[,'Materialb'],[,'Materialc']]

# if (0==len(Material.objects.filter(name='鸡蛋'))):
#     Material.objects.create(name='鸡蛋', number=0,units='个',total=0,remark='无')
# if (0==len(Material.objects.filter(name='面包'))):
#     Material.objects.create(name='面包', number=0,units='个',total=0,remark='无')
# if (0==len(Material.objects.filter(name='馒头'))):
#     Material.objects.create(name='馒头', number=0,units='个',total=0,remark='无')

if (0==len(Member.objects.filter(name='name1'))):
    Member.objects.create(name='name1', funds=0)
if (0==len(Member.objects.filter(name='name2'))):
    Member.objects.create(name='name2', funds=0)
if (0==len(Member.objects.filter(name='name3'))):
    Member.objects.create(name='name3', funds=0)


# Member.objects.create(name='name1', funds=0)
# Member.objects.create(name='name2', funds=0)
# Member.objects.create(name='name3', funds=0)
# Member.objects.create(name='name4', funds=0)

# Member.objects.create(name='breakfast')


def index(request):
    if request.method == 'POST':# 当提交表单时
        form = AddForm(request.POST) # form 包含提交的数据
        if form.is_valid():# 如果提交的数据合法
            # Material_tmp[0] = form.cleaned_data['a']
            # Material_tmp[1] = form.cleaned_data['b']
            # Material_tmp[2] = form.cleaned_data['c']
            # for tmp_i in Material_tmp:  
            #     p = Material.objects.get(name=tmp_i[1])
            #     p.number=p.number+tmp_i[0]
            #     # p.units='个'
            #     # p.total=0;
            #     # p.remark='无'
            #     p.save()
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
    dlist=[]
    dlist.append("<th>name</th> <th>number</th> <th>units</th> <th>total</th> <th>remark</th>")
    for a in d:
        t="<th>%s</th> <th>%s</th> <th>%s</th> <th>%s</th> <th>%s</th>"%(a.name, a.number, a.units, a.total, a.remark)
        dlist.append(t)
    # print dlist[0]
    return render(request,'index.html', {'form': form,'dlist': dlist})

